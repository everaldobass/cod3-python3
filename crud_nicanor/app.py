from tkinter import *
from tkinter import ttk, Button, LabelFrame
import mysql.connector
from src.crudnicanor.conexaoBD import conexao, cursor

#####################################
janela = Tk ()
janela.title ( "Crud com Mysql e Tkinter" )
janela.geometry ( "700x500" )
janela.resizable = False

# Frame
dni = StringVar ()
sexo = StringVar ()
nomes = StringVar ()
apelidos = StringVar ()

modificar = False

############## SELECIONAR OS CAMPOS ###########
def estudanteClick(event):
    id=tbEstudandes.selection()[0]
    if int(id)>0:
        dni.set(tbEstudandes.item(id, "values")[1])
        sexo.set ( tbEstudandes.item ( id, "values" )[2] )
        nomes.set ( tbEstudandes.item ( id, "values" )[3] )
        apelidos.set ( tbEstudandes.item ( id, "values" )[4] )


############## TELA PRINCIPAL ###########
principal: LabelFrame = LabelFrame ( janela, text="Formulário de Estudantes" )
principal.place ( x=50, y=50, width=600, height=400 )



# Labels & Entry
lblDni = Label ( principal, text="DNI" ).grid ( column=0, row=0, padx=5, pady=5 )
txtDni = Entry ( principal, textvariable=dni )
txtDni.grid ( column=1, row=0 )

lblSexo = Label ( principal, text="Sexo" ).grid ( column=0, row=1, padx=5, pady=5 )
txtSexo = ttk.Combobox( principal, values=["M","F"], textvariable=sexo )
txtSexo.grid ( column=1, row=1 )
txtSexo.current(0)

lblNome = Label ( principal, text="Nome" ).grid ( column=2, row=0, padx=5, pady=5 )
txtNome = Entry ( principal, textvariable=nomes )
txtNome.grid ( column=3, row=0 )

lblApelido = Label ( principal, text="Apelido" ).grid ( column=2, row=1, padx=5, pady=5 )
txtApelido = Entry ( principal, textvariable=apelidos )
txtApelido.grid ( column=3, row=1 )


# Mensagem
lblMensagem = Label( principal, text="Aquivos Valores", fg="green" )
lblMensagem.grid ( column=0, row=2, columnspan=4 )


# Tabela de lista de Estudandes
tbEstudandes = ttk.Treeview ( principal, selectmode=NONE )

tbEstudandes["columns"] = ("ID", "DNI", "SEXO", "NOMES", "APELIDOS",)

tbEstudandes.column ( "#0", width=0, stretch=NO )
tbEstudandes.column ( "ID", width=50, anchor=CENTER )
tbEstudandes.column ( "DNI", width=80, anchor=CENTER )
tbEstudandes.column ( "SEXO", width=80, anchor=CENTER )
tbEstudandes.column ( "NOMES", width=150, anchor=CENTER )
tbEstudandes.column ( "APELIDOS", width=200, anchor=CENTER )

tbEstudandes.heading ( "#0", text="" )

tbEstudandes.heading ( "ID", text="ID", anchor=CENTER )
tbEstudandes.heading ( "DNI", text="DNI", anchor=CENTER )
tbEstudandes.heading ( "SEXO", text="SEXO", anchor=CENTER )
tbEstudandes.heading ( "NOMES", text="NOMES", anchor=CENTER )
tbEstudandes.heading ( "APELIDOS", text="APELIDOS", anchor=CENTER )

tbEstudandes.grid ( column=0, row=3, columnspan=10, padx=10 )
tbEstudandes.bind("<<TreeviewSelect>>", estudanteClick)


# ############## BOTÕES ###################
btnEliminar: Button = Button( principal, text="Deletar", command=lambda:Eliminar())
btnEliminar.grid ( column=1, row=4, pady=10, ipadx=20 )

btnCadastrar: Button = Button ( principal, text="Gravar", command=lambda:Cadastrar())
btnCadastrar.grid ( column=2, row=4, pady=10, ipadx=20 )

btnAtualizar: Button = Button ( principal, text="Selecionar", command=lambda:Atualizar())
btnAtualizar.grid ( column=3, row=4, pady=10, ipadx=20 )


# ############## FUNÇÕES ###################
def modificarFalse():
    global modificar
    modificar=False
    tbEstudandes.config(selectmode=None)
    btnCadastrar.config(text="Cadastrar")
    btnAtualizar.config(text="Selecionar")
    btnEliminar.config(state=DISABLED)


############## ATUALIZAR ###################
def modificarTrue():
    global modificar
    modificar=True
    tbEstudandes.config(selectmode=BROWSE)
    btnCadastrar.config(text="Cadastrar")
    btnAtualizar.config(text="Atualizar")
    btnEliminar.config(state=NORMAL)

############## DELETRAR TABELA ###################
def deletar_tabela():
    filas= tbEstudandes.get_children()
    for fila in filas:
        tbEstudandes.delete(fila)

############## PREECHER TABELA ###################
def preencher_tabela():
    deletar_tabela()

    sql="SELECT * FROM estudantes"
    cursor.execute(sql)
    filas = cursor.fetchall()

    for fila in filas:
        id = fila[0]
        tbEstudandes.insert("", END, id, text=id, values=fila )


############## Validar Campos ###########
def validarCampos():
    return len(dni.get()) and len(nomes.get()) and len(apelidos.get())

############## LIMPAR ###################
def limparCampos():
    dni.set ( "" )
    sexo.set ( "" )
    nomes.set ( "" )
    apelidos.set ( "" )

############## DELETAR  #################
def Eliminar():
    id=tbEstudandes.selection()[0]

    if int(id)>0:
        sql = f'DELETE FROM estudantes WHERE id='+id
        cursor.execute(sql)
        conexao.commit()

        tbEstudandes.delete(id)
        lblMensagem.config(text="Deseja deletar o registro? ")

        limparCampos()

    else:
        lblMensagem.config(text="Selecione o registro para deletar! ")


############## NOVO ############
def Cadastrar():
    if validarCampos():
        if modificar ==False:

          dados = dni.get(), sexo.get(), nomes.get(),apelidos.get()
          comando = "INSERT INTO estudantes (dni, sexo, nomes, apelidos) VALUES(%s, %s, %s, %s)"
        # sql = ("INSERT INTO estudantes VALUES(NULL, ?,?,?,?)", (datos))
          cursor.execute(comando, dados)
          conexao.commit()

          lblMensagem.config ( text="Cadastrado corretamente!", fg="green" )

        #deletar_tabela()
        limparCampos ()

    else:
        lblMensagem.config ( text="Favor preencher os campos", fg="red" )
        limparCampos()
    modificarFalse()

def Atualizar():
    if modificar == True:

        id=tbEstudandes.selection()[0]

        dados = dni.get (), sexo.get (), nomes.get (), apelidos.get ()
        comando = "UPDATE estudantes SET dni=%s, sexo=%s, nomes=%s, apelidos=%s WHERE id="+id
        # sql = ("INSERT INTO estudantes VALUES(NULL, ?,?,?,?)", (datos))
        cursor.execute ( comando, dados )
        conexao.commit ()

        lblMensagem.config ( text="Atualizado com sucesso! ", fg="blue" )
        limparCampos ()
    else:
        lblMensagem.config ( text="Favor selecionar uma linha abaixo! ", fg="Orange" )
        limparCampos ()
    modificarTrue()


# Chamar as funções
preencher_tabela()

cursor.close()
conexao.close()


janela.mainloop ()
