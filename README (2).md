# Calculadora em Flet

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)[![Build](https://github.com/oh-my-fish/oh-my-fish/workflows/Build/badge.svg)](https://github.com/oh-my-fish/oh-my-fish/actions?query=workflow%3ABuild)![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[Screencast from 2024-07-28 02-25-31.webm](https://github.com/user-attachments/assets/a025048d-05fb-49de-8468-5b0822c42b07)


Neste estudo de caso, explorei a viabilidade da biblioteca Flet, uma ferramenta incrível para criar aplicativos web, móveis e de desktop em Python. O que mais me impressionou foi a simplicidade de uso e a interatividade proporcionada pela Flet, mesmo sem experiência prévia em desenvolvimento front-end. Além disso, o fato de o Flet ser construído com Flutter, mas sem a necessidade de usar Dart, permite que os aplicativos tenham uma aparência profissional e funcionem em várias plataformas, incluindo Windows, Linux, macOS, dispositivos móveis e web.

Com o Flet, você escreve um único código e pode executá-lo em qualquer sistema. Ele pode ser implantado como um aplicativo da web, visualizado em um navegador ou empacotado como um aplicativo de desktop autônomo para Windows, macOS e Linux. Além disso, é possível instalá-lo como Progressive Web App (PWA) ou usar o aplicativo Flet para iOS e Android. Em resumo, o Flet simplifica o desenvolvimento de aplicativos Python, tornando-os multiusuário e em tempo real.

### Instalação via Poetry
Outra maneira de configurar um ambiente virtual para o seu projeto Flet é usando o Poetry.

Depois de ter o Poetry instalado, execute o seguinte comando no seu terminal:

```bash
poetry new calculadora
```

Esse comando criará um novo diretório chamado "first-flet-app" com a seguinte estrutura:

```
calculadora/
├── pyproject.toml
├── README.md
├── calculadora/
│   └── __init__.py
└── tests/
    └── __init__.py
```

Agora você pode adicionar a dependência do Flet ao seu projeto:

```bash
cd calculadora
poetry add flet
```

Para verificar qual versão do Flet foi instalada:

```bash
poetry run flet --version
```

No arquivo pyproject.toml está as informações de configuração

Agora você está pronto para criar a nossa calculadora.

# Código

Código básico da calculadora, criaremos uma arquivo app.py.

```python
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value="Hello, world!"))

ft.app(target=main)
```
Segundo o tutorial da calculadora, para se criar uma aplciativo multiplataforma não é necessário saber HTML, CSS ou JavaScript, mas precisa de um conhecimento básico de Python e programação orientada a objetos.

## Construção de layout

A construção do layout é basíco:

Para linhas `ft.row`, colunas `ft.Column`, texto `ft.Text` e [botões estilizados](https://flet.dev/docs/getting-started/custom-controls/#styled-controls)`ft.ElevatedButton`

![](/imagens/calc.png)

Logo temos as classes criadas:

Para melhorar o visual dos botões criasse uma classe para estilizar os botões:

```python
class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
```

**`CalcButton`**:
- Essa classe representa um botão genérico na interface da calculadora.
  - Ela herda da classe `ft.ElevatedButton`.
  - O método `__init__` (construtor) aceita dois parâmetros:
     - `text`: O texto exibido no botão.
     - `expand`: Um valor opcional que controla a expansão do botão (padrão é 1).
     Dentro do construtor:
  - Chama o construtor da classe pai (`super().__init__()`).
  - Define a propriedade `self.text` com o texto fornecido.
  - Define a propriedade `self.expand` com o valor fornecido.


Criasse a classe `DigitButton`
```python
class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE
```
**`DigitButton`**:
- Essa classe representa um botão numérico na calculadora.
- Ela herda da classe CalcButton.
- O método __init__ (construtor) aceita dois parâmetros:
  1. text: O texto exibido no botão (por exemplo, “1”, “2”, etc.).
  2. expand: Um valor opcional que controla a expansão do botão (padrão é 1).
  Dentro do construtor:
- Chama o construtor da classe pai (CalcButton.__init__(self, text, expand)).
- Define a cor de fundo (bgcolor) como branco com transparência (WHITE24).
- Define a cor do texto (color) como branco.

Criasse a classe `ActionButton`
```python
class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE
```
**`ActionButton`**:
- Essa classe representa um botão de operação (como +, -, *, /) na calculadora.
- Também herda da classe CalcButton.
- O método __init__ aceita um parâmetro:
  -text: O texto exibido no botão (por exemplo, “+” ou “-”).
  Dentro do construtor:
- Chama o construtor da classe pai (CalcButton.__init__(self, text)).
- Define a cor de fundo (bgcolor) como laranja (ORANGE).
- Define a cor do texto (color) como branco.

Criasse a classe `ExtraActionButton`
```python
class ExtraActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK
```
**`ExtraActionButton`**:
- Essa classe representa botões adicionais (como “AC”, “+/-” e “%”) na calculadora.
- Também herda da classe CalcButton.
- O método __init__ aceita um parâmetro:
  -text: O texto exibido no botão (por exemplo, “AC” ou “%”).
  Dentro do construtor:
- Chama o construtor da classe pai (CalcButton.__init__(self, text)).
- Define a cor de fundo (bgcolor) como cinza-azulado (BLUE_GREY_100).
- Define a cor do texto (color) como preto.

Faça o código e siga a receita de bolo do exemplo.

Para rodar no poetry como aplicativo use o comando:
```python
poetry run python app.py
```

![](/imagens/poetry_run.png)

Para rodar no poetry como aplicativo web use o comando:
```python
poetry run flet run -w app.py
```
[Screencast from 2024-07-28 13-01-10.webm](https://github.com/user-attachments/assets/9baaa27f-cce5-41ea-91e7-865e06126e14)


### Erros no processo e sua solução

Tenho o Ubuntu 24.10 e não sei se você terá o mesmo erro, mas tive o seguite erro:
```bash
/home/edius/.flet/bin/flet-0.23.2/flet/flet: error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory
```

A propósito, instalei o libmujs2 usando o deb vinculado neste relatório de bug, então dei exatamente o mesmo comando que você sugeriu:
```bash
sudo apt install libmpv-dev libmujs-dev libjpeg62
```
Fiz uma busca para descobrir qual pacote deve me fornecer libmpv.so.1, usando apt-file (sudo apt install apt-file) que busca em todos os nomes de arquivos disponíveis em todos os pacotes disponíveis (não apenas instalados):

```bash
apt-file search libmpv.so.1
```
⤷ Nenhum arquivo foi localizado

![](/imagens/apt-file.png)

Mas sendo mais persistente, as coisas mudaram quando eu removo o .1:
```bash
apt-file search libmpv.so
libmpv-dev: /usr/lib/x86_64-linux-gnu/libmpv.so
libmpv2: /usr/lib/x86_64-linux-gnu/libmpv.so.2
libmpv2: /usr/lib/x86_64-linux-gnu/libmpv.so.2.1.0
```
![](/imagens/apt-file search.png)

Como você pode ver, é possível instalar `libmpv.so.2`, mas instalar a `libmpv2` não resolverá o erro sobre `libmpv.so.1` ausente.

Para resolver esse erro entre em `/usr/lib/x86_64-linux-gnu` e então faça `ln -s libmpv.so libmpv.so.1`, depois disso não haverá mais o erro.


## Referências

[Python Flet - Introdução ao Python Flet_Curso de Python Flet][https://www.usandopy.com/pt/curso-de-python-flet/python-flet-introducao-ao-python-flet/]
[Flutter With Python - DEV Community][https://dev.to/ankushsinghgandhi/building-cross-platform-apps-with-flutter-and-python-a-short-guide-using-flet-epa]
[Build multi-platform apps in Python powered by Flutter | Flet][https://flet.dev/]
[Python: Venv e Poetry para criar ambientes virtuais][https://www.alura.com.br/artigos/ven-poetry-no-python]
[Criação de um projeto Python com Poetry][https://aprendendoprogramar.com.br/tutoriais/python/create-app-with-poetry/#criacao-e-configuracao-de-um-projeto-project-setup]
[Usando o Poetry em seus projetos python][https://medium.com/@volneycasas/usando-o-poetry-em-seus-projetos-python-70be5f018281]
[Poetry — Gerenciamento de dependências em Python][https://dev.to/devs-jequie/poetry-gerenciamento-de-dependencias-em-python-4djf]
[https://phylos.net/2023-07-10/python-com-flet](https://phylos.net/2023-07-10/python-com-flet)
