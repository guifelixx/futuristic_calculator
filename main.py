#Criação da interface:
from customtkinter import *

interface = CTk()
interface.title("Calculadora")
interface.geometry("350x400")
interface.resizable(False, False)
set_appearance_mode("system")

#Botões da calculadora:
botao_zero = CTkButton(master=interface,
                       width=80,
                       height=60,
                       text="0",
                       corner_radius=25,
                       fg_color='#585858',
                       hover_color='#151515',
                       command=lambda: func_botoes(0)
                       )
botao_zero.configure(font=('Spoiler Regular', 30))
botao_zero.place(x=94, y=330)

botao_ce = CTkButton(master=interface,
                        width=80,
                        height=60,
                        text="CE",
                        corner_radius=25,
                        fg_color='#B45F04',
                        hover_color='#61380B',
                        command=lambda: clear()
                        )
botao_ce.configure(font=('Spoiler Regular', 30))
botao_ce.place(x=9, y=330)

botao_same = CTkButton(master=interface,
                       width=80,
                       height=60,
                       text="=",
                       corner_radius=25,
                       fg_color='#B45F04',
                       hover_color='#61380B',
                       command=lambda: operacao()
                       )
botao_same.configure(font=('Arial', 15))
botao_same.place(x=179, y=330)

botao_division = CTkButton(master=interface,
                           width=10,
                           height=60,
                           text="÷",
                           corner_radius=30,
                           fg_color='#B45F04',
                           hover_color='#61380B',
                           command=lambda: func_botoes("÷")
                           )
botao_division.configure(font=('Arial', 20))
botao_division.place(x=270, y=330)

botao_seven = CTkButton(master=interface,
                        width=80,
                        height=60,
                        text="7",
                        corner_radius=25,
                        fg_color='#585858',
                        hover_color='#151515',
                        command=lambda: func_botoes(7)
                        )
botao_seven.configure(font=('Spoiler Regular', 30))
botao_seven.place(x=9, y=265)

botao_eigth = CTkButton(master=interface,
                        width=80,
                        height=60,
                        text="8",
                        corner_radius=25,
                        fg_color='#585858',
                        hover_color='#151515',
                        command=lambda: func_botoes(8)
                        )
botao_eigth.configure(font=('Spoiler Regular', 30))
botao_eigth.place(x=94, y=265)

botao_nine = CTkButton(master=interface,
                       width=80,
                       height=60,
                       text="9",
                       corner_radius=25,
                       fg_color='#585858',
                       hover_color='#151515',
                       command=lambda: func_botoes(9)
                       )
botao_nine.configure(font=('Spoiler Regular', 30))
botao_nine.place(x=179, y=265)

botao_less = CTkButton(master=interface,
                       width=10,
                       height=60,
                       text="-",
                       corner_radius=30,
                       fg_color='#B45F04',
                       hover_color='#61380B',
                       command=lambda: func_botoes("-")
                       )
botao_less.configure(font=('Arial', 20))
botao_less.place(x=270, y=265)

botao_four = CTkButton(master=interface,
                       width=80,
                       height=60,
                       text="4",
                       corner_radius=25,
                       fg_color='#585858',
                       hover_color='#151515',
                       command=lambda: func_botoes(4)
                       )
botao_four.configure(font=('Spoiler Regular', 30))
botao_four.place(x=9, y=200)

botao_five = CTkButton(master=interface,
                       width=80,
                       height=60,
                       text="5",
                       corner_radius=25,
                       fg_color='#585858',
                       hover_color='#151515',
                       command=lambda: func_botoes(5)
                       )
botao_five.configure(font=('Spoiler Regular', 30))
botao_five.place(x=94, y=200)

botao_six = CTkButton(master=interface,
                      width=80,
                      height=60,
                      text="6",
                      corner_radius=25,
                      fg_color='#585858',
                      hover_color='#151515',
                      command=lambda: func_botoes(6)
                      )
botao_six.configure(font=('Spoiler Regular', 30))
botao_six.place(x=179, y=200)

botao_more = CTkButton(master=interface,
                       width=10,
                       height=60,
                       text="+",
                       corner_radius=30,
                       fg_color='#B45F04',
                       hover_color='#61380B',
                       command=lambda: func_botoes("+")
                       )
botao_more.configure(font=('Arial', 10))
botao_more.place(x=270, y=200)

botao_one = CTkButton(master=interface,
                      width=80,
                      height=60,
                      text="1",
                      corner_radius=25,
                      fg_color='#585858',
                      hover_color='#151515',
                      command=lambda: func_botoes(1)
                      )
botao_one.configure(font=('Spoiler Regular', 30))
botao_one.place(x=9, y=135)

botao_two = CTkButton(master=interface,
                      width=80,
                      height=60,
                      text="2",
                      corner_radius=25,
                      fg_color='#585858',
                      hover_color='#151515',
                      command=lambda: func_botoes(2)
                      )
botao_two.configure(font=('Spoiler Regular', 30))
botao_two.place(x=94, y=135)

botao_three = CTkButton(master=interface,
                        width=80,
                        height=60,
                        text="3",
                        corner_radius=25,
                        fg_color='#585858',
                        hover_color='#151515',
                        command=lambda: func_botoes(3)
                        )
botao_three.configure(font=('Spoiler Regular', 30))
botao_three.place(x=179, y=135)

botao_multiply = CTkButton(master=interface,
                           width=40,
                           height=60,
                           text="x",
                           corner_radius=30,
                           fg_color='#B45F04',
                           hover_color='#61380B',
                           command=lambda: func_botoes("x")
                           )
botao_multiply.configure(font=('Arial', 15))
botao_multiply.place(x=270, y=135)

#Local onde será feita as contas:
conta = CTkEntry(master=interface,
                 width=330,
                 height=120,
                 corner_radius=10,
                 placeholder_text='0',
                 justify='right'
)
conta.place(relx=0.5, rely=0.17, anchor='center')
conta.configure(font=('Arial', 50))

#Funções para funcionalidades dos botões:
def func_botoes(numero):
    conta.insert("end", numero)

def operacao():
    expressao = conta.get()
    if "+" in expressao:
        operandos = expressao.split("+") #Separa oque é numero e oque é operação aritmética
        resultado = float(operandos[0]) + float(operandos[1]) #Faz a adição
        conta.delete(0, "end")  # Limpa a entrada
        conta.insert(0, str(resultado))  # Exibe o resultado na entrada
    elif "-" in expressao:
        operandos = expressao.split("-")
        resultado = float(operandos[0]) - float(operandos[1])
        conta.delete(0, "end")
        conta.insert(0, str(resultado))
    elif "x" in expressao:
        operandos = expressao.split("x")
        resultado = float(operandos[0]) * float(operandos[1])
        conta.delete(0, "end")
        conta.insert(0, str(resultado))
    elif "÷" in expressao:
        operandos = expressao.split("÷")
        resultado = float(operandos[0]) / float(operandos[1])
        conta.delete(0, "end")
        conta.insert(0, str(resultado))

def clear():
    conta.delete(0, "end")

interface.mainloop()
