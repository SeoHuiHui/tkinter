import tkinter as tk
import tkinter
import tkinter.font


window=tk.Tk()
window.title("COYD")
window.geometry('800x450')
window.resizable(False,False)
window.configure(bg='#1abc9c')

font=tk.font.Font(family="Consolas",size=15,weight=tkinter.font.BOLD)
font1=tk.font.Font(family="Consolas",size=13,weight=tkinter.font.BOLD)
font2=tk.font.Font(family="Consolas",size=20,weight=tkinter.font.BOLD)



photo_resize=photo.resize((250,200))
photo_resize.save('/home/pi/save_folder/product_resize.jpg')




label=tk.Label(window, text="   COYD[판매자]", width=100, height=3,anchor='w', fg="white",bg="#343a40" ,relief="flat",font=font)
label.pack()

label2=tk.Label(window,text='* 상품명 : ',bg="#1abc9c",font=font1)
label2.place(x=70,y=85)
label3=tk.Label(window,text='동일 상품으로 상품 등록이 완료되었습니다.',bg="#1abc9c",font=font1)
label3.place(x=70,y=130)


label4.place(x=90,y=160)

btn=tk.Button(window,text='확인',background='white',width=8,height=1,font=font2)
btn.place(x=315,y=375)


window.mainloop()