import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import customtkinter

def visualizar_notas(matricula):
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
        cursor.execute(f"SELECT id_aluno FROM alunos WHERE matricula = {matricula}")
        aluno_existente = cursor.fetchone()
        if not aluno_existente:
            messagebox.showwarning("Aviso", "ALUNO NÃO EXISTE NO SISTEMA")
            return

        query = (f'SELECT alunos.nome, disciplina.nome_disciplina, notas.nota1, notas.nota2, notas.nota3, notas.media '
                 f'FROM notas INNER JOIN alunos ON alunos.matricula = notas.alunos_matricula '
                 f'INNER JOIN disciplina ON notas.disciplina_id_disciplina = disciplina.id_disciplina '
                 f'WHERE alunos_matricula = {matricula}')
        cursor.execute(query)
        alunos = cursor.fetchall()

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.title("Visualização de Notas")
        root.geometry("600x200+600+200")

        tree = ttk.Treeview(root, columns=("Nome", "Disciplina", "Nota 1", "Nota 2", "Nota 3", "Media"), show="headings", selectmode="extended")
        tree.pack(expand=YES, fill=BOTH)
        tree.heading("Nome", text="Nome")
        tree.column("Nome", minwidth=0, width=100, stretch=NO)
        tree.heading("Disciplina", text="Disciplina")
        tree.column("Disciplina", minwidth=0, width=100, stretch=NO)
        tree.heading("Nota 1", text="Nota 1")
        tree.column("Nota 1", minwidth=0, width=100, stretch=NO)
        tree.heading("Nota 2", text="Nota 2")
        tree.column("Nota 2", minwidth=0, width=100, stretch=NO)
        tree.heading("Nota 3", text="Nota 3")
        tree.column("Nota 3", minwidth=0, width=100, stretch=NO)
        tree.heading("Media", text="Media")
        tree.column("Media", minwidth=0, width=100, stretch=NO)

        style = ttk.Style(root)
        style.theme_use("alt")  # set theme to clam
        style.configure("Treeview", background="gray17",
                        fieldbackground="gray18", foreground="gainsboro")
        style.configure('Treeview.Heading', background="skyblue3")


        for nota in alunos:
            tree.insert("", 0, values=nota, tags=('even',))

        tree.pack()

        root.mainloop()
    except Exception as e:
        print("Erro ao visualizar notas: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def visualizar_notas_interface():
    def visualizar():
        matricula = matricula_entry.get()
        visualizar_notas(matricula)

    root = customtkinter.CTk()
    root.title("Visualização de Notas")
    root.geometry("400x200+400+200")

    customtkinter.CTkLabel(root, text="Matrícula do Aluno:").pack()
    matricula_entry = customtkinter.CTkEntry(root)
    matricula_entry.pack()

    visualizar_button = customtkinter.CTkButton(root, text="Visualizar Notas", command=visualizar)
    visualizar_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    visualizar_notas_interface()