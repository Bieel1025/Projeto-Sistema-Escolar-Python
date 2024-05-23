import visualizacao_notas
import visualizacao_alunos
import cadastro_aluno
import adicao_notas
import customtkinter


def visualizar_alunos():
    visualizacao_alunos.visualizar_alunos()


def cadastrar_aluno():
    cadastro_aluno.cadastrar_aluno_interface()


def adicionar_nota():
    adicao_notas.adicionar_nota_interface()


def visualizar_notas():
    visualizacao_notas.visualizar_notas_interface()


root = customtkinter.CTk()
root.title("Sistema Escolar")
root.geometry("600x400+600+400")

texto = customtkinter.CTkLabel(root, text="")
texto.pack(padx=30, pady=30)

cadastrar_button = customtkinter.CTkButton(root, text="Cadastrar Aluno", command=cadastrar_aluno)
cadastrar_button.pack(padx=5, pady=5)

adicionar_button = customtkinter.CTkButton(root, text="Adicionar Nota", command=adicionar_nota)
adicionar_button.pack(padx=5, pady=5)

visualizar_button = customtkinter.CTkButton(root, text="Visualizar Notas", command=visualizar_notas)
visualizar_button.pack(padx=5, pady=5)

alunos_button = customtkinter.CTkButton(root, text="Alunos", command=visualizar_alunos)
alunos_button.pack(padx=5, pady=5)


root.mainloop()
