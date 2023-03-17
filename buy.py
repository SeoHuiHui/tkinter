from tkinter import *
import tkinter as tk
from turtle import width

import json
import tkinter.font
from tkinter import messagebox
import time

from time import sleep

window=tk.Tk()
window.title('COYD')
window.geometry("800x450")
window.configure(background="YELLOW")
window.resizable(False,False)

# 폰트
font = tk.font.Font(family="Consolas", size=15, weight=tk.font.BOLD)
font2 = tk.font.Font(family="Consolas", size=20, weight=tk.font.BOLD)


buy_key_label = tk.Label(window, text="비밀번호를 입력해주세요 : ", bg="#1abc9c", font=font2)
buy_key_label.place(x=50, y=90)
buy_key_input = tk.Entry(window, width=10, insertwidth=10, bg="#1abc9c", font=font2)
buy_key_input.place(x=400, y=90)


window.mainloop()