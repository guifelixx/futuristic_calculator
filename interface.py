from customtkinter import *
from PIL import Image

interface = CTk()
interface.title("Calculadora")
interface.geometry("350x400")
interface.resizable(False, False)
set_appearance_mode("system")
# interface.iconbitmap(resource_path("images/calc_icon.ico"))

botao_zero = CTkButton(master=interface, width=80, height=60, text="0")
botao_zero.place(x=94, y=330)

botao_ponto = CTkButton(master=interface, width=80, height=60, text=".")
botao_ponto.place(x=9, y=330)

botao_virgula = CTkButton(master=interface, width=80, height=60, text=",")
botao_virgula.place(x=179, y=330)

botao_igual = CTkButton(master=interface, width=80, height=60, text="=")
botao_igual.place(x=264, y=330)

botao_seven = CTkButton(master=interface, width=80, height=60, text="7")
botao_seven.place(x=9, y=265)

botao_eigth = CTkButton(master=interface, width=80, height=60, text="8")
botao_eigth.place(x=94, y=265)

botao_nine = CTkButton(master=interface, width=80, height=60, text="9")
botao_nine.place(x=179, y=265)

botao_less = CTkButton(master=interface, width=80, height=60, text="-")
botao_less.place(x=264, y=265)

botao_four = CTkButton(master=interface, width=80, height=60, text="4")
botao_four.place(x=9, y=200)

botao_five = CTkButton(master=interface, width=80, height=60, text="5")
botao_five.place(x=94, y=200)

botao_six = CTkButton(master=interface, width=80, height=60, text="6")
botao_six.place(x=179, y=200)

botao_more = CTkButton(master=interface, width=80, height=60, text="+")
botao_more.place(x=264, y=200)

botao_one = CTkButton(master=interface, width=80, height=60, text="1")
botao_one.place(x=9, y=135)

botao_two = CTkButton(master=interface, width=80, height=60, text="2")
botao_two.place(x=94, y=135)

botao_three = CTkButton(master=interface, width=80, height=60, text="3")
botao_three.place(x=179, y=135)

botao_multiply = CTkButton(master=interface, width=80, height=60, text="x")
botao_multiply.place(x=264, y=135)

interface.mainloop()
