#!/usr/bin/env python3
"""Mirror the birdcollective.com catalog (Shopify JSON endpoints) into data.json + AVIF images."""
import io, json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

BASE = "https://www.birdcollective.com"
OUT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(OUT, "img")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"}
FULL, THUMB = 1600, 480
QUALITY = 50  # AVIF; visually lossless for product shots at ~35 KB/photo

# Mirrors the site's header navigation (group -> [(collection handle, label)])
NAV = [
    ("Shop", [("new-arrivals", "New Arrivals"), ("womens-bird-shirts", "Women"), ("mens-bird-shirts", "Men"),
              ("kids-bird-tees", "Kids"), ("sale", "Sale")]),
    ("Shop by style", [("birdwatching-apparel", "All Apparel"), ("tees", "T-Shirts"), ("sweatshirts", "Sweatshirts"),
                       ("tanks", "Tanks"), ("long-sleeve-tees", "Long Sleeves")]),
    ("Gear & accessories", [("bird-watching-gear-and-accessories", "All Gear"), ("bird-hats", "Hats"),
                            ("birding-binoculars-binocular-straps", "Binoculars & Straps"), ("bird-socks", "Socks"),
                            ("bird-print-bandanas", "Bandanas"), ("bird-print-bags", "Bags"),
                            ("bird-patch-bird-applique", "Patches"), ("enamel-bird-pins", "Enamel Pins")]),
    ("Home goods", [("home-goods", "All Home Goods"), ("bird-collective-drinkware", "Drinkware"),
                    ("bird-books", "Books & Field Guides"), ("bird-feeders", "Bird Feeders"),
                    ("bird-games", "Games & Puzzles"), ("bird-stickers", "Stickers")]),
    ("Collections", [("pigeon-collection", "Pigeons"), ("puffins", "Puffins"),
                     ("herons-and-egrets-collection", "Herons & Egrets"), ("florida-collection", "Florida"),
                     ("warbler-collection", "Warblers"), ("hummingbird-collection", "Hummingbirds"),
                     ("loons", "Loons"), ("woodpeckers", "Woodpeckers of North America")]),
    ("Shop by bird", [("backyard-bird-shop", "Backyard Birds"), ("sparrows", "Sparrows"),
                      ("shorebirds", "Seabirds & Shorebirds"), ("ducks", "Ducks"), ("raptors", "Raptors"),
                      ("owls", "Owls"), ("wading-birds", "Wading Birds")]),
]


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def paged(path):
    out, page = [], 1
    while True:
        batch = json.loads(get(f"{BASE}{path}?limit=250&page={page}"))["products"]
        out += batch
        if len(batch) < 250:
            return out
        page += 1


def sized(src, w):
    return src + ("&" if "?" in src else "?") + f"width={w}"


def save_image(job):
    src, stem, want_thumb = job
    full, thumb = os.path.join(IMG, stem + ".avif"), os.path.join(IMG, stem + "-t.avif")
    if os.path.exists(full) and (not want_thumb or os.path.exists(thumb)):
        return
    im = Image.open(io.BytesIO(get(sized(src, FULL))))
    im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
    if im.mode == "RGBA":  # flatten transparency onto white
        bg = Image.new("RGB", im.size, "white"); bg.paste(im, mask=im.split()[3]); im = bg
    im.thumbnail((FULL, FULL), Image.LANCZOS)
    im.save(full, "AVIF", quality=QUALITY, speed=6)
    if want_thumb:
        t = im.copy(); t.thumbnail((THUMB, THUMB), Image.LANCZOS)
        t.save(thumb, "AVIF", quality=QUALITY, speed=6)


def text(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html or "", flags=re.S)
    return html


def main():
    os.makedirs(IMG, exist_ok=True)
    products = paged("/products.json")
    print(f"{len(products)} products", file=sys.stderr)

    cats = []
    for group, items in NAV:
        for handle, label in items:
            ids = [p["id"] for p in paged(f"/collections/{handle}/products.json")]
            cats.append({"group": group, "handle": handle, "label": label, "ids": ids})
            print(f"  {group} / {label}: {len(ids)}", file=sys.stderr)

    jobs, out = [], []
    for p in products:
        imgs = []
        for n, im in enumerate(p["images"]):
            stem = f"{p['id']}-{n}"
            jobs.append((im["src"], stem, n < 2))
            imgs.append({"f": stem, "w": im["width"], "h": im["height"], "v": im.get("variant_ids") or []})
        vs = [{"id": v["id"], "t": v["title"], "p": float(v["price"]),
               "c": float(v["compare_at_price"]) if v.get("compare_at_price") else None,
               "a": v["available"]} for v in p["variants"]]
        out.append({
            "id": p["id"], "handle": p["handle"], "title": p["title"], "type": p["product_type"],
            "vendor": p["vendor"], "body": text(p["body_html"]), "created": p["created_at"][:10],
            "options": [{"name": o["name"], "values": o["values"]} for o in p.get("options", [])
                        if o["name"] != "Title"],
            "variants": vs, "images": imgs,
        })

    print(f"{len(jobs)} images", file=sys.stderr)
    with ThreadPoolExecutor(8) as ex:
        for i, _ in enumerate(ex.map(save_image, jobs), 1):
            if i % 100 == 0:
                print(f"  {i}/{len(jobs)}", file=sys.stderr)

    known = {p["id"] for p in out}
    for c in cats:
        c["ids"] = [i for i in c["ids"] if i in known]
    data = {"source": BASE, "fetched": time.strftime("%Y-%m-%d"), "nav": cats, "products": out}
    with open(os.path.join(OUT, "data.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    main()
