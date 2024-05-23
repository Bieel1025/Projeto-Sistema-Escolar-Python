import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import customtkinter


def visualizar_alunos():
    try:
        global connection
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

        deletar_button = customtkinter.CTkButton(root, text="Deletar Aluno", command=deletar_alunos_interface)
        deletar_button.place(x=150, y=250)

        recarregar_button = customtkinter.CTkButton(root, text="Recarregar Tabela", command=visualizar_alunos)
        recarregar_button.place(x=300, y=250)



        root.mainloop()

    except Exception as e:
        print("Erro ao visualizar alunos: ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def deletar_alunos(matricula):
    try:
        cursor = connection.cursor()
        # Verifica se a matricula existe
        cursor.execute(f"SELECT id_aluno FROM alunos WHERE matricula = {matricula}")
        matricula_existente = cursor.fetchone()
        if not matricula_existente:
            messagebox.showwarning("Aviso", "MATRICULA NAO EXISTE NO SISTEMA")
            return

        #Deleta o aluno da tabela
        query = (f"DELETE FROM alunos WHERE matricula = {matricula}")
        cursor.execute(query)
        connection.commit()

        messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar matricula '{matricula}'" )

def deletar_alunos_interface():
    def visualizar():
        matricula = matricula_entry.get()
        deletar_alunos(matricula)

    root1 = customtkinter.CTk()
    root1.title = ("Deletar aluno")
    root1.geometry("400x400+400+400")

    customtkinter.CTkLabel(root1, text="Matrícula do Aluno:").pack()
    matricula_entry = customtkinter.CTkEntry(root1)
    matricula_entry.pack()

    deletar_button = customtkinter.CTkButton(root1, text="Deletar Aluno", command=visualizar)
    deletar_button.pack(padx=10, pady=10)

    root1.mainloop()


if __name__ == "__main__":
    deletar_alunos_interface()

