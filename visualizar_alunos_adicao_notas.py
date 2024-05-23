import tkinter as tk
from tkinter import ttk
import mysql.connector
import customtkinter


def visualizar_alunos():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="colegio",
            auth_plugin="mysql_native_password"
        )
        cursor = connection.cursor()

        query = "SELECT nome, matricula FROM alunos ORDER BY id_aluno"
        cursor.execute(query)
        alunos = cursor.fetchall()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.title("Visualização de Alunos")
        root.geometry("600x300+600+300")

        tree = ttk.Treeview(root, columns=("Nome", "Matricula"), show="headings")
        tree.heading("Nome", text="Nome")
        tree.heading("Matricula", text="Matricula")

        for i in alunos:
            tree.insert("", "end", values=i)

        style = ttk.Style(root)
        style.theme_use("alt")  # set theme to clam
        style.configure("Treeview", background="gray17",
                        fieldbackground="gray18", foreground="gainsboro")
        style.configure('Treeview.Heading', background="skyblue3")

        tree.pack()

        root.mainloop()

    except Exception as e:
        print("Erro ao visualizar alunos: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
