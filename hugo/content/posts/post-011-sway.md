---
title: "do i3 para o Sway"
date: 2021-02-22
draft: false
toc: false
images:
tags:
  - untagged
---

# Motivação

Uma das poucas coisas que me fariam mudar de ideia de trocar de sistema operacional, window manager ou qualquer software que eu uso no computador, com certeza, é velocidade/performance (por isso que, normalmente, não gosto de aplicações feitas em Electron, pois costumam ser bem devagar).

E, visto que o Sway é a transição mais tranquila para usuários i3, porém com um twist bem importante para a performance, pois utiliza o wayland no lugar do xorg.

# Dificuldades

Mas, nem tudo são flores. Apesar de eu ser super baunilha (sempre usei o Manjaro com i3 do jeito que veio), existem alguns programas bem específicos que eu uso no meu dia a dia. Eles são:

- Synergy (sério, tenho múltiplos computadores ligados na mesa.)
- Flameshot
- xmodmap

O resto, eu realmente não liguei muito e minha configuração antiga do i3 serviu muito bem no Sway. Mas, nesses programas eu tive um bom atrito (um deles eu ainda não encontrei substituto).

# Flameshot

O problema foi resolvido com a sugestão de um colega meu do trabalho, com o combo de aplicações: grim, slurp e swappy. Que, honestamente, funciona melhor que o Flameshot no aspecto de edição da imagem antes de exportar. 

```
    bindsym $mod+p exec grim -g "$(slurp)" - | swappy -f -
```

# xmodmap

No meu computador de trabalho eu não tive dificuldades, pois eu utilizei um teclado mecânico completamente configurável. E, com isso, consegui deixar as teclas do jeito que eu queria:

- Troca do Capslock por Ctrl
- Troca das teclas vizinhas do espaço pelos Supers (Mod4)

Já no meu laptop pessoal, eu tenho um computador que comprei no Japão. E, por esse motivo, ele tem um teclado diferente. Possui teclas adicionais:

- Muhenkan (No conversion)
- Henkan (Convert)
- Kana Mode

Eu aproveito essas teclas para transformar no Super (Mod4), que são teclas muito importante para gerenciamento de janelas em windows managers de tiling (colocação?). E, como eu usava um arquivo .Xmodmap para configurar essas teclas e o wayland não aceita mais essas teclas, eu tive que criar o seguinte arquivo `~/.xkb/symbols/jp-mod`

```
partial modifier_keys
xkb_symbols "basic" {
  include "us(intl)"
  key <MUHE> { [ Super_L ] };
  key <HENK> { [ Super_R ] };
  modifier_map Mod4 { <MUHE>, <HENK> };
};
```

E faço referência no arquivo de configuração do Sway `~/.config/sway/config`

```
input * {
  xkb_layout jp-mod
  xkb_options caps:ctrl_modifier
}
```

# Synergy

Infelizmente não existe substituto que funcione como o Synergy ou próximo disso. E, fazer ele funcionar no wayland é um esforço bem grande.

Se você realizar uma busca na internet vai encontrar uma discussão sobre a compatibilidade do Synergy para o wayland de 2014. Sim, 2014:

- https://github.com/symless/synergy-core/issues/4090

E, toda issue aberta sobre isso, é automaticamente fechada e o CEO da empresa garante que isso está no roadmap para a próxima grande release deles:

- https://symless.com/synergy/roadmap

Algo que está sendo prometido desde 2014 e deu em feijoada até agora. Duvido muito que vamos ver algo dessa portabilidade em um futuro próximo.

Pesquisando alternativas encontrei algo que faz um KVM bem meia boca de maneira virtual que não depende do xorg ou do wayland para funcionar: 

- https://github.com/htrefil/rkvm

Porém, diversas pessoas reportaram que não funciona. E, de fato, não funcionou para mim também. A única coisa que acontece, é travar o seu computador assim que sobe o server. Alguém, aparentemente, conseguiu mapear o problema, mas sem sucesso de fazer funcionar.

# Conclusão

Estou gostando bastante do Sway, mesmo não conseguindo utilizar 100% todas as aplicações que eu tinha acesso antigamente. Mas, mesmo assim, ainda acho que vale a pena a troca da falta do Synergy para a performance que ele prove.

Para quem tiver curiosidade:

- https://swaywm.org/


