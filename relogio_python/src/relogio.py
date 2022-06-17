# ***********************************************************
# BY NAME:Everaldo Nascimento
# PROJECT: Como Criar Relógio Digital em Python
# v: 1.0.0
# Autor:Usando Python
# https://youtu.be/TknTtYa0yYI
# https://www.1001fonts.com/digital-7-font.html
# ***********************************************************

from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("./src/digital-7/digital-7.ttf")

###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul
# Cores
fundo = cor1
cor = cor6
# Janela
janela = Tk()
janela.title("")
janela.geometry("600x280")
janela.resizable(width=False, height=False)
janela.configure(bg=cor1)

# Função
def relogio():
    # Variaveis
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   " +str(dia) + "/" + str(mes) + "/" + str(ano))
    l3.config(text="Everaldo Nascimento")

l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2 = Label(janela, text="", font=("digital-7 18"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

l3 = Label(janela, text="", font=("Arial 16"), bg=fundo, fg=cor)
l3.grid(row=2, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()
