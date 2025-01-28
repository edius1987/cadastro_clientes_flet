# Sistema de Cadastro de Clientes com Flet

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)

Este projeto demonstra um sistema simples de cadastro de clientes desenvolvido com Python e Flet, permitindo operações básicas de CRUD (Create, Read, Delete) usando SQLite como banco de dados.

## Funcionalidades

- Adicionar novos clientes (nome e CPF)
- Listar todos os clientes cadastrados
- Remover clientes pelo CPF
- Interface gráfica intuitiva
- Armazenamento persistente em SQLite

## Instalação

### Usando Poetry (Recomendado)

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd [nome-do-diretorio]
```

2. Instale as dependências com Poetry:
```bash
poetry install
```

3. Execute o aplicativo:
```bash
poetry run python cadastro_clientes_flet.py
```

### Instalação Manual

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install flet
pip install sqlite3
```

## Executando o Aplicativo

### Como Aplicativo Desktop
```bash
poetry run python cadastro_clientes_flet.py
```

### Como Aplicativo Web
```bash
poetry run flet run -w cadastro_clientes_flet.py
```

## Solução de Problemas

Se você estiver usando Ubuntu e encontrar o erro relacionado à `libmpv.so.1`, siga estes passos:

1. Instale as dependências necessárias:
```bash
sudo apt install libmpv-dev libmujs-dev libjpeg62
```

2. Crie um link simbólico:
```bash
cd /usr/lib/x86_64-linux-gnu
sudo ln -s libmpv.so libmpv.so.1
```

## Tecnologias Utilizadas

- Python
- Flet (Interface gráfica)
- SQLite (Banco de dados)
- Poetry (Gerenciamento de dependências)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
