---
title: viação cometa alert
layout: post
category: blog
date: 2020-09-07
---

# Viação Cometa Alert

![viação cometa alerter](post-004-cover.webp)
(a aplicação.)

Devido ao Covid-19 e a política de quarentena para amenizar as mortes e a queda do sistema de saúde pública aqui no Brasil, muitos comércios fecharam seu funcionamento. Porém, depois de um tempo, tivemos um afrouxamento da quarentena e a algumas empresas começaram a voltar a funcionar. Porém, aos poucos e com cuidado.

Uma das categorias de negócios mais afetada foi o transporte. Com a quarentena, não tem muito sentido as pessoas utilizarem transporte no geral, não sendo essencial. Por esse motivo, viagens foram canceladas e futuras passagens impedidas de serem compradas.

Antes da pandemia aparecer em nossa dimensão, eu estava me encontrando com uma pessoa e, depois de tanto esperar (pacientemente), pude ver que as passagens começaram a serem vendidas novamente. Porém, reparei na minha repetição de entrar no site para verificar a disponibilidade de passagens. E vi a oportunidade de poder automatizar isso. Com isso em mente, surgiu a idéia de criar uma aplicação que faz essa verificação para mim.

# O Plano

Nada de muito complicado. O fluxo seria o seguinte:

- verificação de passagens no site
- alertar os horários pelo whatsapp

Simples assim. Apenas dois passos.

# O site

Imaginei que precisaria fazer o tratamento do HTML do site. Porém, para a minha alegria, isso não seria necessário, uma vez que existe um endpoint que o front consulta, deixando tudo bem mais fácil.

Logo abaixo dá para ver que um simples GET já é possível receber o JSON com as cidades que a empresa trabalha.

``` sh
$ http https://www.viacaocometa.com.br/content/jca/cometa/pt-br/jcr:content.getDestinos.json?origem=467
HTTP/1.1 200 OK
X-Vhost: www.viacaocometa.com.br

{
    "listaLocalidade": {
        "erro": {
            "descricaoAlerta": "",
            "descricaoErro": "",
            "ocorreuAlerta": false,
            "ocorreuErro": false,
            "sessionValid": true
        },
        "lsLocalidade": [
            {
                "cidade": "A PRATA",
                "id": 443,
                "uf": "SP"
            },
            {
                "cidade": "AMERICANA",
                "id": 64,
                "uf": "SP"
            },
            ...
             {
                "cidade": "ÁGUAS DA PRATA",
                "id": 14,
                "uf": "SP"
            }
        ]
    }
}
```

E então, depois de facilitar muito o meu trabalho retornando um JSON, foi simplesmente configurar como enviar uma mensagem pelo Whatsapp.

# Whatsapp

Para isso, já tem uma galera que fez um excelente trabalho de simular todo o Whatsapp Web, deixando só o trabalho de chamar uma função para enviar uma mensagem (a única ação que eu precisaria, uma vez que eu não estou fazendo um bot de conversa).

Precisei autorizar o uso do meu número (utilizando o QR Code). Após isso, foi só configurar o destinatário e pronto. Nesse caso, eu fiz para mandar mensagem para mim mesmo.

https://github.com/Rhymen/go-whatsapp

![viação cometa alerter](post-004-msg.webp)

# CronJob

Para fazer a verificação de tempos em tempos pensei em diversas estratégias.

A primeira estratégia foi em utilizar o:

https://github.com/robfig/cron

Porém, para deixar a aplicação cuidar disso, eu precisaria que ele precisasse ficar rodando indefinitivamente. Com o risco da aplicação morrer ou qualquer outra instabilidade acontecer, preferi passar a responsabilidade para o sistema operacional. Nesse caso, o Linux.

Como o Go não possui muitos problemas em executar os binários gerados pelo Go, então isso não seria um problema também.

# Github

Para quem tiver curiosidade em verificar o código da aplicação simples que eu fiz, segue o link:

https://github.com/denislee/viacaocometa-alert


