import tkinter
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from visualizar_alunos_adicao_notas import visualizar_alunos
from tkinter import *
import customtkinter


def adicionar_nota(matricula, nota1, nota2, nota3, disciplina):
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
        # Verifica se a disciplina pro aluno já existe
        cursor.execute(f"SELECT id_notas FROM notas WHERE alunos_matricula = {matricula} AND "
                       f"disciplina_id_disciplina = {disciplina}")
        disciplina_aluno_existente = cursor.fetchall()
        if disciplina_aluno_existente:
            messagebox.showwarning("Aviso", "NOTA DE ALUNO JÁ ESTA CADASTRADA PARA ESSA DISCIPLINA")
            return

        query = (f'INSERT INTO notas (alunos_matricula, disciplina_id_disciplina, nota1, nota2, nota3)'
                 f'VALUES ({matricula}, {disciplina}, {nota1}, {nota2}, {nota3})')

        cursor.execute(query)

        media = (float(nota1) + float(nota2) + float(nota3)) / 3
        mediaL = round(media, 1)

        query = f'UPDATE notas SET media = {mediaL} WHERE alunos_matricula = {matricula} AND disciplina_id_disciplina = {disciplina}'
        cursor.execute(query)

        connection.commit()
        messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar nota: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def adicionar_nota_interface():
    root = customtkinter.CTk()
    root.title("Adição de Nota")
    root.geometry("600x400+600+400")

    customtkinter.CTkLabel(root, text="Matrícula do Aluno:").pack()
    matricula_entry = customtkinter.CTkEntry(root)
    matricula_entry.pack(side=TOP)

    valor = customtkinter.StringVar(root)
    valor.set("Selecione a disciplina")
    caixa_disciplina = customtkinter.CTkOptionMenu(master=root, values=["ciencias", "física", "geografia", "história",
                                                "literatura", "matemática", "português", "quimica"], variable=valor,
                                                   corner_radius=10, )
    caixa_disciplina.pack(padx=5, pady=5)

    customtkinter.CTkLabel(root, text="Nota 1:").pack()
    nota1_entry = customtkinter.CTkEntry(root)
    nota1_entry.pack(side=TOP)

    customtkinter.CTkLabel(root, text="Nota 2:").pack()
    nota2_entry = customtkinter.CTkEntry(root)
    nota2_entry.pack(side=TOP)

    customtkinter.CTkLabel(root, text="Nota 3:").pack()
    nota3_entry = customtkinter.CTkEntry(root)
    nota3_entry.pack(side=TOP)

    def adicionar():
        matricula = matricula_entry.get()
        nota1 = nota1_entry.get()
        nota3 = nota3_entry.get()
        nota2 = nota2_entry.get()
        disciplina = valor.get()
        if disciplina == "física":
            disciplina=5
        elif disciplina == "biologia":
            disciplina=9
        elif disciplina == "ciencias":
            disciplina =7
        elif disciplina == "geografia":
            disciplina =3
        elif disciplina == "história":
            disciplina =4
        elif disciplina == "literatura":
            disciplina =8
        elif disciplina == "matemática":
            disciplina =2
        elif disciplina == "português":
            disciplina =1
        elif disciplina == "quimica":
            disciplina =6

        adicionar_nota(matricula, nota1, nota2, nota3, disciplina)

    adicionar_button = customtkinter.CTkButton(root, text="Adicionar Nota", command=adicionar)
    adicionar_button.pack(padx=5, pady=5)

    alunos_button = customtkinter.CTkButton(root, text="Alunos", command=visualizar_alunos)
    alunos_button.pack(padx=5, pady=5)

    root.mainloop()



if __name__ == "__main__":
    adicionar_nota_interface()