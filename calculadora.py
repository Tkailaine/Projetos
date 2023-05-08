#importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk

#função entrada
def entrada(b):
    global todos_botoes

    todos_botoes = todos_botoes + str(b)
    #passando valor para a calculadora
    valor_texto.set(todos_botoes)


#def calcular
def calcular():
    resultado = eval(todos_botoes)
    valor_texto.set(resultado)

#função limpar
def limpar():
    global todos_botoes
    todos_botoes = ''
    valor_texto.set(todos_botoes)


#cores
cor1 = "#383636" #cinza escuro
cor2 = "#fc9300" #amarelo alaranjado
cor3 = "#ffffff" #branco
cor4 = "#a6030e" #vermelho
cor5 = "#dcdee0" #cinza claro

#criação da janela
janela = Tk()
#definindo título da janela
janela.title('Calculadora')
#definindo o tamanho da janela
janela.geometry('235x315')

#designer da tela
janela.config(bg=cor1)
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

todos_botoes = ''

#string valor
valor_texto = StringVar()

#criação do label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2,font="Ivy 18", anchor="e", padx=7, justify=RIGHT, relief=FLAT, bg=cor1, fg=cor5)
app_label.place(x=0, y=0)

#criação do frame corpo da calculadora
frame_corpo = Frame(janela, width=235, height=270)
frame_corpo.grid(row=1, column=0)

#criando botões da calculadora
b_01 = Button(frame_corpo, command= limpar, text="C", width=11, height=2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE, bg=cor5)
b_01.place(x=0, y=0)
b_02 = Button(frame_corpo, command= lambda:entrada('%'), text="%", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_02.place(x=115, y=0)
b_03 = Button(frame_corpo, command= lambda:entrada('/'), text="/", width=5, height=2, bg=cor2, fg=cor3, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_03.place(x=175, y=0)

b_04= Button(frame_corpo, command= lambda:entrada('7'), text="7", width=5, height=2,bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_04.place(x=0, y=53)
b_05= Button(frame_corpo, command= lambda:entrada('8'),text="8", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_05.place(x=57, y=53)
b_06=Button(frame_corpo, command= lambda:entrada('9'),text="9", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_06.place(x=115, y=53)
b_07= Button(frame_corpo, command= lambda:entrada('*'),text="*", width=5, height=2, bg=cor2, fg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_07.place(x=175, y=53)

b_08=Button(frame_corpo,command= lambda:entrada('6'), text="6", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_08.place(x=0, y=106)
b_09= Button(frame_corpo,command= lambda:entrada('5'), text="5", width=5, height=2, bg=cor5,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_09.place(x=57, y=106)
b_10=Button(frame_corpo,command= lambda:entrada('4'), text="4", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=115, y=106)
b_11=Button(frame_corpo, command= lambda:entrada('-'), text="-", width=5, height=2, bg=cor2, fg=cor3, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_11.place(x=175, y=106)

b_12=Button(frame_corpo,command= lambda:entrada('3'), text="3", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)
b_13=Button(frame_corpo,command= lambda:entrada('2'), text="2", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=57, y=159)
b_14=Button(frame_corpo,command= lambda:entrada('1'), text="1", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_14.place(x=115, y=159)
b_15=Button(frame_corpo,command= lambda:entrada('+'), text="+", width=5, height=2, bg=cor2, fg=cor3, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_15.place(x=175, y=159)

b_16= Button(frame_corpo,command= lambda:entrada('0'), text="0", width=11, height=2, bg=cor5,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)
b_17=Button(frame_corpo,command= lambda:entrada('.'), text=".", width=5, height=2, bg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_17.place(x=115, y=212)
b_18=Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor2, fg=cor3, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_18.place(x=175, y=212)


#execução da janela
janela.mainloop()
entrada()