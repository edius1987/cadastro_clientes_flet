# -*- coding: utf-8 -*-

import flet as ft
import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('clientes.db', check_same_thread=False)
cursor = conn.cursor()

# Criar a tabela de clientes se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL
)
''')
conn.commit()

# Função para adicionar um novo cliente
def adicionar_cliente(nome, cpf):
    try:
        cursor.execute("INSERT INTO clientes (cpf, nome) VALUES (?, ?)", (cpf, nome))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # CPF já existe

# Função para listar todos os clientes
def listar_clientes():
    cursor.execute("SELECT cpf, nome FROM clientes")
    return cursor.fetchall()

# Função para remover um cliente pelo CPF
def remover_cliente(cpf):
    cursor.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
    conn.commit()
    return cursor.rowcount > 0

# Interface gráfica com Flet
def main(page: ft.Page):
    page.title = "Cadastro de Clientes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def adicionar_cliente_click(e):
        nome = nome_field.value
        cpf = cpf_field.value
        if nome and cpf:
            if adicionar_cliente(nome, cpf):
                resultado_text.value = "Cliente adicionado com sucesso!"
            else:
                resultado_text.value = "Erro: CPF já existe."
            nome_field.value = ""
            cpf_field.value = ""
            page.update()
        else:
            resultado_text.value = "Por favor, preencha todos os campos."
            page.update()

    def listar_clientes_click(e):
        clientes = listar_clientes()
        lista_clientes.controls.clear()
        for cpf, nome in clientes:
            lista_clientes.controls.append(ft.Text(f"Cliente: {nome}, CPF: {cpf}"))
        page.update()

    def remover_cliente_click(e):
        cpf = cpf_remover_field.value
        if cpf:
            if remover_cliente(cpf):
                resultado_text.value = "Cliente removido com sucesso!"
            else:
                resultado_text.value = "Erro: CPF não encontrado."
            cpf_remover_field.value = ""
            page.update()
        else:
            resultado_text.value = "Por favor, insira o CPF."
            page.update()

    # Campos de entrada para adicionar cliente
    nome_field = ft.TextField(label="Nome", width=300)
    cpf_field = ft.TextField(label="CPF", width=300)
    adicionar_button = ft.ElevatedButton(text="Adicionar Cliente", on_click=adicionar_cliente_click)

    # Lista de clientes
    lista_clientes = ft.Column()

    # Campo de entrada para remover cliente
    cpf_remover_field = ft.TextField(label="CPF do Cliente a Remover", width=300)
    remover_button = ft.ElevatedButton(text="Remover Cliente", on_click=remover_cliente_click)

    # Texto de resultado
    resultado_text = ft.Text()

    # Layout da página
    page.add(
        ft.Column([
            ft.Text("Adicionar Cliente", size=20, weight=ft.FontWeight.BOLD),
            nome_field,
            cpf_field,
            adicionar_button,
            ft.Divider(),
            ft.Text("Listar Clientes", size=20, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton(text="Listar Clientes", on_click=listar_clientes_click),
            lista_clientes,
            ft.Divider(),
            ft.Text("Remover Cliente", size=20, weight=ft.FontWeight.BOLD),
            cpf_remover_field,
            remover_button,
            ft.Divider(),
            resultado_text
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

# Iniciar a aplicação Flet
ft.app(target=main)
