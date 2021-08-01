from Add import addition
from tkinter import *
from Learn import learning
from Detected import checking

root = Tk()
root.geometry('400x150')
root.title('Распознавание лиц')

name_label = Label(text="Введите идентификатор:")
surname_label = Label(text="Введите ФИО:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

txt = Entry(root,width=35)  
txt.grid(column=1, row=0)
txt1 = Entry(root,width=35)  
txt1.grid(column=1, row=1)

btn = Button(root, text="Добавить",activebackground="#2A4BF3",bg="#4763F0",width="10", fg="white", command=lambda: addition(txt, txt1))  
btn.place(x=274,y=45)
btn.pack
  
btn1 = Button(root, text="Применить", activebackground="#2A4BF3",bg="#4763F0",width="10", fg="white", command=learning)  
btn1.place(x=274, y=78)
  
btn2 = Button(root, text="Проверить",activebackground="#2A4BF3",bg="#4763F0",width="10", fg="white", command=checking)  
btn2.place(x=274,y=111)

root.mainloop()

