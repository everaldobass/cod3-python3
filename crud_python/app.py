# ***********************************************************
# BY NAME:Everaldo Nascimento
# PROJECT:CRUD em Python com SQLite|Formulário Python Tkinter 
# v: 1.0.0
#
# Autor:Usando Python
# https://youtu.be/7N25wyyJ7pc
# https://doc.qt.io/qtforpython/licenses.html
# ***********************************************************

################# IMPORTANDO #########

from cgitb import text
import email
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import Tree
from tkcalendar import Calendar, DateEntry


# Importando controler
from controller import *

################# CORES ##############

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

#################INTERFACE GRÁFICA ##########

janela = Tk()
janela.title("Curso do Tkinter")
janela.geometry("1280x650")
janela.configure(background=co9)
janela.resizable(width=False, height=False)

################# Frame Janela ##############
frame_cima = Frame(janela, width=350, height=50, bg=co2, relief='flat' )
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=350, height=600, bg=co1, relief='flat' )
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=930, height=600, bg=co1, relief='flat' )
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

################# Frame Cima ##############
app_nome = Label(frame_cima, text='Formulário de Cadastro', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat' )
app_nome.place(x=15, y=20)

# Variaveis Global
global tree

# Função Inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    dia = e_calend.get()
    estado = e_estado.get()
    obs = e_obs.get()

    lista = [nome, email, telefone, dia, estado, obs]

    if nome =='':
        messagebox.showerror('Erro', 'Preencher todos os campos!')

    else:
  
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Dados salvos!')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calend.delete(0,'end')
        e_estado.delete(0,'end')
        e_obs.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

    


    # Função Atualizar Tabela
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calend.delete(0,'end')
        e_estado.delete(0,'end')
        e_obs.delete(0,'end')

        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])
        e_calend.insert(0,tree_lista[4])
        e_estado.insert(0,tree_lista[5])
        e_obs.insert(0,tree_lista[6])

        # Update _ Atualizar
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            dia = e_calend.get()
            estado = e_estado.get()
            obs = e_obs.get()

            lista = [nome, email, telefone, dia , estado, obs, valor_id]

            if nome =="" :
                messagebox.showerror('Erro', "Preencher todos os campos! ")

            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', "Os dados foram atualizados! ")

                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_calend.delete(0,'end')
                e_estado.delete(0,'end')
                e_obs.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

                mostrar()

        # Botão Atualizar
        btn_confirmar = Button(frame_baixo, command=update, text= 'Confirmar', width=10, font=('Ivy 8 bold'), bg=co8,  fg=co1, relief='raised', overrelief='ridge' )
        btn_confirmar.place(x=130, y=370)

    except IndexError: 
        messagebox.showinfo('Sucesso', "Dados atualizados! ")



        # Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Dados', "Deletados com sucesso! ")

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError: 
           messagebox.showerror('Erro', "Preencher todos os campos! ")

               



################# Frame Baixo ##############
# Nome
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_nome.place(x=15, y=10)
e_nome = Entry(frame_baixo, width=40, justify='left', relief='flat' )
e_nome.place(x=15, y=40, height=30)

# Email
l_email = Label(frame_baixo, text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_email.place(x=15, y=70)
e_email = Entry(frame_baixo, width=40, justify='left', relief='flat' )
e_email.place(x=15, y=100, height=30)


# Telefone
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_telefone.place(x=15, y=130)
e_telefone = Entry(frame_baixo, width=40, justify='left', relief='flat' )
e_telefone.place(x=15, y=160, height=30)


#Data Consulta
l_calend = Label(frame_baixo, text='Data Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_calend.place(x=15, y=190)
e_calend = DateEntry(frame_baixo, width=12, background='darkgray', foreground='white', borderwhidth=2 )
e_calend.place(x=15, y=220)


# Estado
l_estado = Label(frame_baixo, text='Estado Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=22, justify='left', relief='flat' )
e_estado.place(x=160, y=220, height=30)

# Observação
l_obs = Label(frame_baixo, text='Observação: *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat' )
l_obs.place(x=15, y=260)
e_obs = Entry(frame_baixo, width=40, justify='left', relief='flat' )
e_obs.place(x=15, y=290, height=30)

# Botão Inserir
btn_inserir = Button(frame_baixo, command=inserir, text="Inserir", width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
btn_inserir.place(x=15, y=340)

# Botão Atualizar
btn_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
btn_atualizar.place(x=125, y=340)

# Botão Deletar
btn_deletar = Button(frame_baixo, command=deletar, text="Deletar", width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
btn_deletar.place(x=235, y=340)


#------------------- Codigo Tabela Direita ----------------

def mostrar():
    # Global
    global tree
    
    # Chamando a função Selecionar os dados.
    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'Email','Telefone', 'Data', 'Estado','Observações']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")


    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

     # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[40,180,180,100,110,100,200]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
    
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)




# Chamando a Tabela mostrar
mostrar()

janela.mainloop()