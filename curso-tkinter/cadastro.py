from tkinter import *
from tkinter import messagebox, Menu, Button
from tkinter import ttk
import sqlite3

###################### JANELA ###########################
root = Tk ()
root.title ( "Aplicação Tkinter" )
root.geometry ( "800x400" )
root.resizable ( width=False, height=False )

id = StringVar ()
nome = StringVar ()
cargo = StringVar ()
salario = StringVar ()


############################ CONEXAO COM O BANCO #########################

def conexao():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()

    try:
        con.execute ( '''
            CREATE TABLE funcionarios(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME VARCHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL)
        ''' )
        messagebox.showinfo ( "Conectado ", "Base de dados criada com sucesso!" )
    except:
        messagebox.showinfo ( "Conectado ", "Base de dados já existe!" )


############################ ELIMINAR #########################

def eliminar():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()

    if messagebox.askyesno ( message="Deseja Excluir a tabela de funcuinarois?", title="ADVERTECNIA" ):
        con.execute ( "DROP TABLE funcionarios" )

    else:
        pass

    limparCampos ()
    mostrar ()


############################ SAIR DO BANCO ######################

def sair():
    valor = messagebox.askquestion ( "Sair", "Deseja sair da aplicação?" )
    if valor == "Yes":
        root.destroy ()


########################### LIMPAR CAMPOS ######################

def limparCampos():
    id.set ( "" )
    nome.set ( "" )
    cargo.set ( "" )
    salario.set ( "" )


########################### MENSSAGEM ##########################

def mensagem():
    sobre = '''
    Aplicação CRUD
    Versão 1.0
    Author : Everaldo Nascimento
    Tecnologia: Tkinter
    Licença: GPL
    '''
    messagebox.showinfo ( title="INFORMACION", message=sobre )


########################### MÉTODOS PARA CRIAR / ATUALIZAR /  ###

def criar():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()
    try:
        datos = nome.get (), cargo.get (), salario.get ()
        con.execute ( "INSERT INTO funcionarios VALUES(NULL,?,?,?)", (datos) )
        conexao.commit ()
    except:
        messagebox.showwarning ( "ADVERTENCIA", "Ocorreu um error, favor verificar conexao! " )
        pass

    limparCampos ()
    mostrar ()


########################### MOSTRAR DADOS #######################

def mostrar():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()

    registros = tree.get_children ()

    for elemento in registros:
        tree.delete ( elemento )

    try:
        con.execute ( "SELECT * FROM funcionarios" )
        for row in con:
            tree.insert ( "", 0, text=row[0], values=(row[1], row[2], row[3]) )
    except:
        pass


###################### TABELA AREA ########################

tree = ttk.Treeview ( height=10, columns=('#0', '#1', '#2') )
tree.place ( x=0, y=130 )
tree.column ( '#0', width=100 )
tree.heading ( '#0', text="ID", anchor=CENTER )
tree.column ( '#1', width=300 )
tree.heading ( '#1', text="Nome Funcionarios", anchor=CENTER )
tree.heading ( '#2', text="Cargo", anchor=CENTER )
tree.column ( '#3', width=200 )
tree.heading ( '#3', text="Salário", anchor=CENTER )


def selecionarUsandoClick(event):
    item.tree.identify ( 'item', event.x, event.y )
    id.set ( tree.item ( item, "text" ) )
    nome.set ( tree.item ( item, "values" )[0] )
    cargo.set ( tree.item ( item, "values" )[1] )
    salario.set ( tree.item ( item, "values" )[2] )

    tree.bind ( "Double-1", selecionarUsandoClick )


########################### ATUALIZAR #########################

def atualizar():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()

    try:
        datos = nome.get (), cargo.get (), salario.get ()
        con.execute ( "UPDATE funcionarios SET NOME=?, CARGO=?, SALARIO=? WHERE ID="+id.get (), (datos) )
        conexao.commit()
    except:
        messagebox.showwarning ( "ADVERTENCIA", "Ocorreu um error, ao atualizar os registros " )
        pass
    limparCampos ()
    mostrar ()


########################### DELETRAR #########################

def deletar():
    conexao = sqlite3.connect ( 'banco.db' )
    con = conexao.cursor ()
    try:
        if messagebox.askyesno ( message="Deseja realmente deletar o registro? ", title="ADVERTENCIA" ):
            con.execute ( "DELETE FROM funcionarios WHERE ID="+id.get())
            conexao.commit ()
    except:
        messagebox.showwarning ( "ADVERTENCIA", "Ocorreu um error, ao atualizar os registros " )
        pass

        limparCampos ()
        mostrar ()


###################### MENUS ############################

menubar = Menu ( root )
menubar_set = Menu ( menubar, tearoff=0 )
menubar_set.add_command ( label="Conectar", command=conexao )
menubar_set.add_command ( label="Excluir", command=eliminar () )
menubar_set.add_command ( label="Sair", command=sair () )
menubar.add_cascade ( label="Home", menu=menubar_set )

menubar_ajuda = Menu ( menubar, tearoff=0 )
menubar_ajuda.add_command ( label="Limpar os campos", command=limparCampos () )
menubar_ajuda.add_command ( label="Sobre", command=mensagem () )
menubar.add_cascade ( label="Ajuda", menu=menubar_ajuda )

########################### CAIXA DE TEXTOS ###########################
entrada = Entry ( root, textvariable=id )

# NOME
label_nome = Label ( root, text="Nome: " )
label_nome.place ( x=50, y=10 )
entrada_nome = Entry ( root, textvariable=nome, width=60 )
entrada_nome.place ( x=100, y=10 )

# Cargo
label_cargo = Label ( root, text="Cargo: " )
label_cargo.place ( x=50, y=40 )
entrada_cargo = Entry ( root, textvariable=cargo )
entrada_cargo.place ( x=100, y=40 )

# SALÁRIO
label_salario = Label ( root, text="Salário: " )
label_salario.place ( x=280, y=40 )
entrada_salario = Entry ( root, textvariable=salario, width=20 )
entrada_salario.place ( x=340, y=40 )

# VALORES
label_moeda = Label ( root, text="BR" )
label_moeda.place ( x=520, y=40 )

########################### CRIANDO BOTÕES ###########################
btnCadastar = Button( root, text="Cadastrar", command=criar )
btnCadastar.place( x=50, y=90 )

btnAtualizar = Button( root, text="Atualizar", command=atualizar )
btnAtualizar.place( x=180, y=90 )

btnMostrar = Button( root, text="Mostrar", bg="blue", command=mostrar )
btnMostrar.place( x=320, y=90 )

btnDeletar = Button( root, text="Deletar", bg="red", command=deletar )
btnDeletar.place( x=450, y=90 )


root.config( menu=menubar )

root.mainloop ()
