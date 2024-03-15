from customtkinter import *
from PIL import Image

interface = CTk()
interface.title("Calculadora")
interface.geometry("350x400")
interface.resizable(False, False)
set_appearance_mode("system")
# interface.iconbitmap(resource_path("images/calc_icon.ico"))

botao_zero = CTkButton(master=interface, width=80, height=60, text="0",corner_radius=25, fg_color='#808080')
botao_zero.configure(font=('Spoiler Regular', 30))
botao_zero.place(x=94, y=330)

botao_ponto = CTkButton(master=interface, width=80, height=60, text=".", corner_radius=25, fg_color='#080632')
botao_ponto.configure(font=('Spoiler Regular', 30))
botao_ponto.place(x=9, y=330)

botao_same = CTkButton(master=interface, width=80, height=60, text="=", corner_radius=25,fg_color='#080632')
botao_same.configure(font=('Arial', 15))
botao_same.place(x=179, y=330)

botao_division = CTkButton(master=interface, width=10, height=60, text="/", corner_radius=30, fg_color='#080632')
botao_division.configure(font=('Arial', 20))
botao_division.place(x=270, y=330)

botao_seven = CTkButton(master=interface, width=80, height=60, text="7", corner_radius=25, fg_color='#808080')
botao_seven.configure(font=('Spoiler Regular', 30))
botao_seven.place(x=9, y=265)

botao_eigth = CTkButton(master=interface, width=80, height=60, text="8", corner_radius=25, fg_color='#808080')
botao_eigth.configure(font=('Spoiler Regular', 30))
botao_eigth.place(x=94, y=265)

botao_nine = CTkButton(master=interface, width=80, height=60, text="9", corner_radius=25, fg_color='#808080')
botao_nine.configure(font=('Spoiler Regular', 30))
botao_nine.place(x=179, y=265)

botao_less = CTkButton(master=interface, width=10, height=60, text="-", corner_radius=30, fg_color='#080632')
botao_less.configure(font=('Arial', 20))
botao_less.place(x=270, y=265)

botao_four = CTkButton(master=interface, width=80, height=60, text="4", corner_radius=25, fg_color='#808080')
botao_four.configure(font=('Spoiler Regular', 30))
botao_four.place(x=9, y=200)

botao_five = CTkButton(master=interface, width=80, height=60, text="5", corner_radius=25, fg_color='#808080')
botao_five.configure(font=('Spoiler Regular', 30))
botao_five.place(x=94, y=200)

botao_six = CTkButton(master=interface, width=80, height=60, text="6", corner_radius=25, fg_color='#808080')
botao_six.configure(font=('Spoiler Regular', 30))
botao_six.place(x=179, y=200)

botao_more = CTkButton(master=interface, width=10, height=60, text="+", corner_radius=30, fg_color='#080632')
botao_more.configure(font=('Arial', 10))
botao_more.place(x=270, y=200)

botao_one = CTkButton(master=interface, width=80, height=60, text="1", corner_radius=25, fg_color='#808080')
botao_one.configure(font=('Spoiler Regular', 30))
botao_one.place(x=9, y=135)

botao_two = CTkButton(master=interface, width=80, height=60, text="2", corner_radius=25, fg_color='#808080')
botao_two.configure(font=('Spoiler Regular', 30))
botao_two.place(x=94, y=135)

botao_three = CTkButton(master=interface, width=80, height=60, text="3", corner_radius=25, fg_color='#808080')
botao_three.configure(font=('Spoiler Regular', 30))
botao_three.place(x=179, y=135)

botao_multiply = CTkButton(master=interface, width=10, height=60, text="x", corner_radius=30, fg_color='#080632')
botao_multiply.configure(font=('Arial', 15))
botao_multiply.place(x=270, y=135)

interface.mainloop()
