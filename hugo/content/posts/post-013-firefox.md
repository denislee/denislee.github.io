---
title: "firefox"
date: 2021-02-27
draft: false
toc: false
images:
tags:
  - firefox 
  - browser
---

# Motivação

O meu antigo navegador é o qutebrowser (como eu havia descrito no post anterior) e infelizmente eu estive tendo alguns problemas com ele.

- crashes constantes
- travamento do meu computador todo (teclado e mouse pararam de funcionar)

Acredito que esses já são bons motivos para ver alternativas.

# Alternativas

Os meus navegadores favoritos sempre foram:

- Firefox
- Brave
- Wyeb

Porém, sempre gostei mais do firefox (só para ficar o mais longe do Chrome possível).

Logo na minha primeira busca já encontrei esse link sobre como alterar o firefox para ficar com a cara do qutebrowser

https://github.com/aadilayub/firefox-i3wm-theme

Era exatamente o que eu precisava. Mas, ainda pretendo buscar mais algumas soluções na internet. De todo modo, vou deixar aqui as instruções dele:

# Firefox i3 Theme

![](screenshot.png)

A theme for Firefox meant to emulate [qutebrowser](http://qutebrowser.org) and integrate with the i3 window manager.

## Install & configuration instructions

Before installing the theme:

- Install the [Tridactyl](https://addons.mozilla.org/en-US/firefox/addon/tridactyl-vim/) firefox extension

- Go in the "Customize" section of firefox and remove the new tab button from the navigation bar, and also set "Density" to "Compact".

- [Enable userChrome.css in about:config](https://www.youtube.com/watch?v=levqpofIJ_k&feature=youtu.be)

To install the theme:

1. Go to `about:support` in Firefox.

2. Application Basics > Profile Directory > Open Directory.

3. Open directory in a terminal.

4. Create a chrome directory if it doesn't exist:

```
mkdir -p chrome
cd chrome
```

5. Copy the `userChrome.css` file from this repository to that folder


For best results, install the [Jetbrains Mono](https://www.jetbrains.com/lp/mono/) font

---

CSS based on [0xbiel's dotfiles](https://github.com/0xbiel/dotfiles/blob/master/userChrome.css)


O CSS:

```

@namespace "http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul";

/* Hide close button on tabs */
#tabbrowser-tabs .tabbrowser-tab .tab-close-button { display:none !important; }

#TabsToolbar, .tabbrowser-tab {
  max-height: 20px !important;
  font-size: 11px;
}

:root:not([customizing]) #TabsToolbar{
  background-color: #000000;
}

:root:not([customizing]) #navigator-toolbox {
  background-color: #000000 !important;
}

/* Hide window controls on fullscreen */
#window-controls { display: none; }

/* Change color of normal tabs */

tab:not([selected="true"]) { 
  background-color: #222222 !important;
  color: #888888 !important;
  border: none;
}

/* tab font */
tab { font-family: 'Jetbrains Mono', monospace; border: none; }

/* safari style tab width */  
.tabbrowser-tab[fadein]{ max-width: 100vw !important; border: none }

/* hide nav bar */
/* #nav-bar { visibility: collapse; } */

/* auto-hide nav-bar (nav-bar shows when F6 is pressed)*/
  #navigator-toolbox {
    -moz-appearance: none;
    background-color: transparent !important;
    border-top: none;
  }
  .browser-toolbar:not(.titlebar-color),
  #tabbrowser-tabs:not([movingtab])
    > .tabbrowser-arrowscrollbox
    > .tabbrowser-tab
    > .tab-stack
    > .tab-background[multiselected='true']:-moz-lwtheme,
  #tabbrowser-tabs:not([movingtab])
    > .tabbrowser-arrowscrollbox
    > .tabbrowser-tab
    > .tab-stack
    > .tab-background[selected='true']:-moz-lwtheme,
  * {
    /* --tab-line-color: var(--color1); */
    /* --tab-min-width: 76px; */
  }
  #urlbar, #navigator-toolbox #searchbar {border: none !important;}

  #urlbar:not(.megabar):not([focused='true']):-moz-lwtheme,
  #urlbar.megabar:not([focused='true']):-moz-lwtheme > #urlbar-background,
  #navigator-toolbox #searchbar:not(:focus-within):-moz-lwtheme,
  #navigator-toolbox {
    border: none !important;
  }
  #urlbar:not(.megabar):-moz-lwtheme,
  #urlbar.megabar:-moz-lwtheme > #urlbar-background,
  #navigator-toolbox #searchbar:-moz-lwtheme {
    background-color: var(--background) !important;
  }
  #navigator-toolbox {
    --tabs-border-color: var(--background) !important;
  }

  toolbox {
    z-index: 10;
    margin-top: 0px !important;
    margin-bottom: -30px !important;
    height: 0 !important;
    pointer-events: none;
  }
  vbox {pointer-events: all;}


  #nav-bar {
    opacity: 0;
    transform-origin: 0 0;
    pointer-events: none;
    transition: transform, ease-in-out 0.2s, opacity 0.2s ease-in-out !important;
  }
  /* All the states in which the URL bar is visible */
  toolbox:focus-within > #nav-bar {
    opacity: 1;
    transform: none;
    pointer-events: all;
  }

/* end auto hide nav-bar */

/* debloat navbar */

  #back-button { display: none; }

  #forward-button { display: none; }

  #reload-button { display: none; }

  #stop-button { display: none; }

  #home-button { display: none; }

  #downloads-button { display: none; }

  #library-button { display: none; }

  #sidebar-button { display: none; }

  /* Firefox account button */
  #fxa-toolbar-menu-button { display: none; }

  #nav-bar-overflow-button { display: none !important; }

  /* General Firefox menu button */
  #PanelUI-button { display: none; }

  /* Empty space before and after the url bar */
  #customizableui-special-spring1,
  #customizableui-special-spring2 { display: none; }
  /* style navbar */
  #nav-bar,
  #navigator-toolbox {
    border-width: 0 !important;
  }

/* end debloat navbar */

/* remove megabar */
  /* https://github.com/WesleyBranton/Remove-Firefox-Megabar/blob/master/remove_megabar.css */
  
  /* REMOVE MEGABAR START
   * VERSION 1.0.4
   * CODE AT: http://userchrome.wesleybranton.com/megabar
   * RELEASE NOTES: http://userchrome.wesleybranton.com/notes/megabar */
  @-moz-document url(chrome://browser/content/browser.xhtml) {
      /* DISABLE EXPANDING START */
      #urlbar[breakout][breakout-extend] {
          top: calc((var(--urlbar-toolbar-height) - var(--urlbar-height)) / 2) !important;
          left: 0 !important;
          width: 100% !important;
      }
  
      #urlbar[breakout][breakout-extend] > #urlbar-input-container {
          height: var(--urlbar-height) !important;
          padding-block: 0 !important;
          padding-inline: 0 !important;
      }
      /* DISABLE EXPANDING END */
  }
  /* REMOVE MEGABAR END */

/*  */

/* style urlbar */
  #urlbar-container {
    --urlbar-container-height: var(--tab-min-height) !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    font-family: 'Jetbrains Mono', monospace;
    font-size: 11px;
  }

  #urlbar {
    --urlbar-height: var(--tab-min-height) !important;
    --urlbar-toolbar-height: var(--tab-min-height) !important;
    min-height: var(--tab-min-height) !important;
  }

  #urlbar-background {
    border-width: 0 !important;
    border-radius: 0 !important;
  }

  #urlbar-input-container {
    border-width: 0 !important;
    margin-left: 1em !important;
  }

  #urlbar-input {
    margin-left: 0.4em !important;
    margin-right: 0.4em !important;
  }

  .urlbarView-row {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    line-height: var(--urlbar-height) !important;
  }

  .urlbarView-row-inner {
    padding-top: 0.3em !important;
    padding-bottom: 0.3em !important;
    height: var(--urlbar-height) !important;
  }

  .urlbarView-favicon {
    height: 1em !important;
    width: 1em !important;
    margin-bottom: 0.2em !important;
  }
  
/* debloat urlbar */
  #tracking-protection-icon-container { display: none; }

  #identity-box { display: none; }

  #reader-mode-button { display: none; }

  #pageActionButton { display: none; }

  #pocket-button { display: none; }

  #star-button { display: none; }

  #urlbar-zoom-button { display: none; }

  /* Go to arrow button at the end of the urlbar when searching */
  #urlbar-go-button { display: none; }

  /* Bottom left page loading status or url preview */
  #statuspanel { display: none !important; }
/* end debloat urlbar */


/* hide tab bar if only one tab open */
tab:only-of-type { display: none; }

/* remove min-height from tabs toolbar (needed for fullscreen one tab) */
#TabsToolbar, #tabbrowser-tabs, #tabbrowser-tabs > .tabbrowser-arrowscrollbox, #tabbrowser-arrowscrollbox {
  min-height: 0 !important; 
}

/* Tab: selected colors */

#tabbrowser-tabs .tabbrowser-tab[selected] .tab-content { 
  background: #285577 !important;
  color: #ffffff !important;
  border: none !important;
}

/* Tab: hovered colors */

#tabbrowser-tabs .tabbrowser-tab:hover:not([selected]) .tab-content {
  background: #285577 !important;
  color: #ffffff !important;
}

/* remove white margin around active tabs */
#tabbrowser-tabs:not([movingtab]) > #tabbrowser-arrowscrollbox > .tabbrowser-tab[beforeselected-visible]::after, #tabbrowser-tabs[movingtab] > #tabbrowser-arrowscrollbox > .tabbrowser-tab[visuallyselected]::before,
.tabbrowser-tab[visuallyselected]::after {
  border: none !important;
}

/*AGENT_SHEET*/
#main-window #navigator-toolbox #TabsToolbar:not(:-moz-lwtheme){
  background: #285577 !important;
}

/* hide favicons */
.tabbrowser-tab .tab-icon-image {
  display: none !important;
}

/* show favicon if tab is pinned */
.tabbrowser-tab[pinned] .tab-icon-image {
  display: inline !important;
}

/* hide window controls */
.titlebar-buttonbox-container { display: none; }

```
