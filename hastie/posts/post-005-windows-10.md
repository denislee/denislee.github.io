---
title: windows 10, but better
layout: post
category: blog
date: 2020-09-09
---

# Windows 10, but better

![windows 10](post-005-cover.webp)

*(Windows 10)*

Depois de passar por muitos problemas com a conectividade do Windows 10, finalmente decidi fazer algo a respeito. Descobri através de alguns vídeos na internet que existe uma versão do Windows mais limpo, ou seja, sem todo o aparato de telemetría e spyware que a Microsoft deixa em seu sistema operacional.

Os videos que eu assisti foram:

*We fixed Windows 10 - Microsoft will HATE this!*
https://www.youtube.com/watch?v=nwkiU6GG-YU

*Windows 10 for Power Users – Private, Secure, Zero Bloatware (Windows 10 Ameliorated)*
https://www.youtube.com/watch?v=YTL0i5XzS7k

Tutorial escrito pelo Wolfgang
https://notthebe.ee/Windows10.html

E para facilitar, segui um híbrido de tutorial escrito do Wolfgang, quanto o vídeo dele. Ambos acabam complementando um ao outro. Mas, um parece nao funcionar sem o outro. Infelizmente.

Por esse motivo, estou deixando as minhas anotações da instalação aqui também. (Para futuros usos pessoais também.) Que basicamente será uma transcrição em português do que já foi escrito pelo Wolfgang, porém com as minhas observações.

## Resumo dos arquivos necessários

1. ISO do Windows 10 completo (peguei a versão Pro)
2. ISO do Linux (pode ser qualquer um)
3. Aplicação para calcular o SHA1 da imagem
4. Aplicação para criar um pendrive bootável
5. Atualização do Windows 10 cumulativo
6. Atualização do Windows 10 incremental
7. Amelioration Script
8. Backup dos seus Drivers
9. Hardentools (Security without borders)

## Download da imagem do Windows 10

Faça download da imagem do Windows 10

**Alternativa 1** Baixar o aplicativo Fido (funciona apenas no Windows) https://github.com/pbatard/Fido

**Alternativa 2**: Selecionar no site https://tb.rg-adguard.net/public.php

No caso, eu peguei a versao em ingles e pro. Importante ressaltar que nessa hora que apenas nessa hora que você poderá escolher a língua. Caso queira trocar futuramente, precisará reinstalar o Windows (acredito que você não queira fazer isso).

## Verificação da imagem do Windows 10

Para verificar se a imagem do Windows que você acabou de baixar não está corrompida ou alterada precisamos de uma aplicação para calcular o hash.

**Alternativa 1**: Utilização da ferramenta já existente no PowerShell

```
Get-FileHash -Algorithm SHA1 Windows_2004.iso
```

**Alternativa 2**: https://www.adaic.org/resources/add_content/standards/articles/SHA-1.html

Executando alguma dessas duas alternativas, será possível comparar a saida desses programas no site: https://sha1.rg-adguard.net/

## Download dos updates

Para isso você devera entrar no site o Windows 10 Update History: https://support.microsoft.com/en-us/help/4555932/windows-10-update-history

1. Procurar a sua versão do Windows. na primeira coluna da esquerda.

2. Depois clique na primeiro item da segunda coluna na esquerda (In this release)

3. Copie o código do titulo da pagina KBXXXXXXX e va no site https://www.catalog.update.microsoft.com/Home.aspx e procure por esse código

4. Faça download da arquitetura do seu processador e para o seu Windows (cuidado para não baixar a versão para servidor)

5. Volte para a pagina onde você copiou o código (KBXXXXXXX) e procure pela palavra chave: `the latest SSU` 

6. Copie o código que vem logo em seguida dessa palavra que você procurou e vá para o site e faça download (passos 3. e 4. anteriores)

No fim, você terá baixado dois arquivos de atualização do Windows

## Download do script AME

**Alternativa 1**: https://git.ameliorated.info/malte/scripts/releases/download/1903.2020.03.06/amelioration_1903_2020.03.06.bat

Caso o link esteja desatualizado. Entre no site https://ameliorated.info/documentation.html#ame_pre e procure pela palavra chave `Windows 10 Amelioration script` e faça download

## Backup dos seus drivers

Abra o PowerShell como Admin e execute o comando

```
pnputil /export-driver * "C:\backup-drivers"
```

## Hora de baixar o Linux

No tutorial ele (Wolfgang) recomendou baixar o xubuntu. Segui a recomendação, porém descobri na prática que qualquer imagem funciona. Poderia até ser um Arch, mas acredito que a recomendação foi mais pela facilidade de uso mesmo. A exigência para facilitar e que você consiga acessar a internet facilmente e tenha a modalidade de boot dentro do Linux sem instalar o mesmo.

https://xubuntu.org/

## Criando um pendrive bootável

Precisamos baixar um programa para gravar o ISO do Windows no pendrive e deixar ele bootável. Para isso recomendo você baixar o seguinte programa

**Alternativa 1**: https://rufus.ie/

Abra o Rufus e escolha o drive que está conectado o seu Pendrive, escolha a ISO do Windows e pronto.

## Copiando os arquivos

Copie todos os arquivos que você baixou até agora para dentro do Pendrive. Segue a lista que deve entrar

- ISO do linux
- Rufus
- Atualizações do Windows

## Instalando o Windows

Agora os passos para iniciar a instalação na sua máquina

1. Conecte o Pendrive no seu computador
2. Reinicie o mesmo
3. Desative toda e qualquer conexão com a internet (wifi e ethernet) pela bios
4. Troque a ordem do boot para iniciar pelo pendrive
5. Talvez seja necessário desativar o boot de seguranca
6. Instale o Windows

## Primeiro boot no Windows

Responda não para todas as perguntas de compartilhamento de informação que eles perguntarem durante o setup final da instalação do Windows.

Assim que você já estiver dentro do sistema operacional, faça as seguintes ações:

- Faca unpin em todos os aplicativos da barra de tarefas.
- Faca unpin em todos os aplicativos do menu do botão iniciar.
- Remova a barra de busca da barra de tarefas.

## Instalação das atualizações

Crie os seguintes diretórios no drive de onde foi instalado o Windows:

```
- C:\SSU
- C:\Cumulative
```

Abra o PowerShell com permissão de administrador e dentro dele entre no drive do pendrive. E faça os seguintes comandos:

```
expand -F:* name_of_the_ssu_package.msu C:\SSU
expand -F:* name_of_the_cumulative_package.msu C:\Cumulative
```

Em seguida faça o seguinte comando para instalar os pacotes descompactados

```
dism /online /add-package /packagepath=C:\SSU\name_of_the_ssu.cab
```

Vai reiniciar apos a instalacao. Depois de reiniciado instale a atualização cumulativa

```
dism /online /add-package /packagepath=C:\Cumulative\name_of_the_cumulative.cab
```

Reinicie duas vezes e agora execute o comando final


```
dism /online /Cleanup-Image /StartComponentCleanup
```

## Executando o script AME

Clique com o botão direito no script e execute como administrador.

**Escolha 1**: `Run Pre-Amelioration`

- Espere o processo terminar.

**Escolha 3**: `User Permissions`

- Altere a senha de administrador.

- Altere os privilégios do seu usuário local para `Standard User`

Faça logout e logue novamente.

Abre um PowerShell como administrador e execute o comando para alterar a sua senha:


```
net user <seu-usuário> *
```

## Criação do mídia de boot do Linux

Abra o Rufus e escolha o pendrive e o ISO do Linux para transformar o seu pendrive que você acabou de usar para instalar o Windows para instalar o Linux.

Reinicie o computador com o pendrive conectado.

## Dentro do Linux

Nessa parte você já pode ligar novamente toda a conectividade do seu computador (que você havia desativado anteriormente na BIOS).

Entre no Linux pela escolha que não precisa instalar nada.

Abra um terminal e entre no diretório raiz da instalação do seu Windows e faça o seguinte comando:


```
wget https://git.ameliorated.info/malte/scripts/releases/download/1903.2020.03.06/ameliorate_1903_2020.03.06.sh
```
(esse link pode estar desatualizado. Nesse caso entre no link: https://ameliorated.info/documentation.html e procure pela palavra chave `Linux Ameliorate script` e copie o link)

Agora é só executar o script.

Caso tenha problemas em executar o script, faça os seguintes passo:

```
sed -i 's/\r$//' <script-shell>
```

Agora é só executar o script que você acabou de baixar e aguardar


## Post-Amelioration

Edite o script AME que você usou antes de entrar no Linux e procure pela seguinte linha:

```
choco install -y --force --allow-empty-checksums firefox thunderbird vlc youtube-dl 7zip open-shell jpegview vcredist-all directx onlyoffice
```

E substitua para:

```
choco install -y --force --allow-empty-checksums firefox thunderbird vlc youtube-dl 7zip open-shell  -installArgs ADDLOCAL=StartMenu jpegview vcredist-all directx libreoffice
```

Execute o script e escolha o Post-Amelioration


## Hardening Windows Settings

Para ajudar na segurança, baixe e instale o Harden Tools.

**Alternativa 1**: https://securitywithoutborders.org/tools/hardentools.html

## Reinstalação dos drivers

```
pnputil.exe /add-driver C:\backup-drivers\*.inf /subdirs /install /reboot
```

