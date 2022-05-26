import tkinter as tk
import sqlite3
import pandas as pd


# Funções
def cadastrar():
    # Conexão com o banco de dados
    conexao = sqlite3.connect('clientes.db')
    con = conexao.cursor()

    # Criando a tabela no banco
    con.execute("INSERT INTO clientes VALUES(:nome, :sobrenome, :email, :telefone)",
                {
                    'nome': entry_nome.get(),
                    'sobrenome': entry_sobrenome.get(),
                    'email': entry_telefone.get(),
                    'telefone': entry_email.get()

                }
    )

    # Confirmando
    conexao.commit()
    # Fechar o banco de dados
    conexao.close()

    # Limpando os dados depois do cadastro
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


def exportar():
    # Conexão com o banco de dados
    conexao = sqlite3.connect('clientes.db')
    con = conexao.cursor()

    # Criando a tabela no banco
    con.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = con.fetchall()
    #print(clientes_cadastrados)
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'id'])
    #clientes_cadastrados.to_csv('exporta_clientes.csv')
    clientes_cadastrados.to_excel('export_clientes_excel.xlsx')

    # Confirmando
    conexao.commit()
    # Fechar o banco de dados
    conexao.close()



# Criando a Janela
janela = tk.Tk()
janela.title("Cadastro de clientes")
janela.geometry("450x400")

# Labels
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='E-mail')
label_telefone.grid(row=2, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Telefone')
label_email.grid(row=3, column=0, padx=10, pady=10)

# Entry
entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10, ipadx=80,ipady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10, ipadx=80,ipady=10)

entry_telefone = tk.Entry(janela, text='E-mail', width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10, ipadx=80,ipady=10)

entry_email = tk.Entry(janela, text='Telefone', width=30)
entry_email.grid(row=3, column=1, padx=10, pady=10, ipadx=80,ipady=10)

# Botões
btn_cadastrar = tk.Button(janela, text='Cadastrar', command= cadastrar, fg="white", bg="gray" )
btn_cadastrar.grid(row=4, column=0, padx=10, pady=10,ipadx=120, ipady=10, columnspan=2)

btn_exportrar = tk.Button(janela, text='Exportar', command= exportar, fg="white", bg="gray" )
btn_exportrar.grid(row=5, column=0, padx=10, pady=10, ipadx=120,ipady=10 ,columnspan=2)

janela.mainloop()


def cadastro_cliente():
    return None