---
title: "Qutebrowser"
date: 2021-02-22
draft: false
toc: false
images:
tags:
  - qutebrowser
  - browser
---

# Motivação

Como todo usuário de Vim e agraciado pelas suas teclas de atalho, além do window manager que melhor atende suas necessidades e potencializa o seu aprendizado no Vim, o navegador seria o próximo a ser beneficiado por essa memória muscular de navegação: hjkl.

Por isso, a escolha mais comum de navegador seria o qutebrowser. Seguem algumas configurações (pequenas) que eu fiz, para deixar ele minimamente utilizável.

# Configurações

Você poderá editar o arquivo `.config/qutebrowser/config.py` diretamente ou gerar/salvar um arquivo com o comando `:config-save-py --force`

E para editar as configurações correntes pelo próprio navegador com o comando: `:set` e depois salvar usando o `:config-save-py --force`

Seguem as configurações que eu deixo:

# url.searchengines

```
c.url.searchengines = {'DEFAULT': 'https://www.startpage.com/do/dsearch?query={}'}
```

# content.notifications

```
c.content.notifications = False
```

# content.geolocation

```
c.content.notifications = False
```


