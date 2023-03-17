from tkinter import *
import tkinter as tk
from tkinter.tix import INTEGER
from turtle import width
import tkinter.font
from tkinter import messagebox

window = tk.Tk()
window.title("COYD")
window.geometry('800x450')
window.resizable(False, False)
window.configure(bg='#1abc9c')
text = tkinter.Text(window)

# 폰트적용
font = tk.font.Font(family="Consolas", size=15, weight=tk.font.BOLD)
font2 = tk.font.Font(family="Consolas", size=20, weight=tk.font.BOLD)

equa = ""
equation = tk.StringVar()


def btnPress(num):
    global equa
    sale_key_input.delete(0, tk.END)
    equa = equa + str(num)
    equation.set(equa)
    sale_key_input.insert(0, str(equa))


def ClearPress():
    sale_key_input.delete(0, END)


def EnterPress():
    global equa
    global save_key
    total = str(eval(equa))
    equation.set(total)
    save_key = str(eval(equa))
    window.destroy()



label1 = tk.Label(window, text="   COYD[판매자]", width=100, height=3, anchor='w', fg="white", bg="#343a40",
                  relief="flat", font=font)
label1.pack()

sale_key_label = tk.Label(window, text="인증번호를 입력해주세요 : ", bg="#1abc9c", font=font2)
sale_key_label.place(x=150, y=90)
sale_key_input = tk.Entry(window, width=10, insertwidth=10, bg="#1abc9c", font=font2)
sale_key_input.place(x=500, y=90)


# clear버튼
Clear = tk.Button(window, text="C", bg='white', command=ClearPress, height=3, width=15, borderwidth=1, relief=tk.SOLID)
Clear.place(x=220, y=360)

# enter 버튼(확인)
Enter = tk.Button(window, text="확인", bg='white', command=EnterPress, height=3, width=15, borderwidth=1, relief=tk.SOLID)
Enter.place(x=460, y=360)

window.mainloop()
