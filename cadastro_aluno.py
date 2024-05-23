# cadastro_aluno.py

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import customtkinter


def cadastrar_aluno(nome, matricula):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="colegio",
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor()

        # Verifica se o aluno já existe
        cursor.execute("SELECT id_aluno FROM alunos WHERE nome = %s OR matricula = %s", (nome, matricula))
        aluno_existente = cursor.fetchone()
        if aluno_existente:
            messagebox.showwarning("Aviso", "ALUNO JÁ EXISTE NO SISTEMA")
            return

        # Insere o aluno na tabela
        query = "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)"
        values = (nome, matricula)
        cursor.execute(query, values)

        connection.commit()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar aluno: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def cadastrar_aluno_interface():
    root = customtkinter.CTk()
    root.title("Cadastro de Aluno")
    root.geometry("400x200+400+200")

    customtkinter.CTkLabel(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
    nome_entry = customtkinter.CTkEntry(root)
    nome_entry.grid(row=0, column=1, padx=10, pady=10)

    customtkinter.CTkLabel(root, text="Matrícula:").grid(row=1, column=0, padx=10, pady=10)
    matricula_entry = customtkinter.CTkEntry(root)
    matricula_entry.grid(row=1, column=1, padx=10, pady=10)

    # cadastrar aluno
    def cadastrar():
        nome = nome_entry.get()
        matricula = matricula_entry.get()
        cadastrar_aluno(nome, matricula)

    # cadastrar aluno
    cadastrar_button = customtkinter.CTkButton(root, text="Cadastrar", command=cadastrar)
    cadastrar_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    cadastrar_aluno_interface()