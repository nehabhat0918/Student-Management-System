from tkinter import *
from PIL import ImageTk
window=Tk()

window.geometry("1740x700+0+0")
window.backgroundImage=ImageTk.PhotoImage(file=r"C:\Users\whynew.in\OneDrive\Desktop\python\PES\UNIT-3\image\b2.jpg")
bglabel=Label(window,image=window.backgroundImage)
bglabel.place(x=0,y=0)

loginFrame=Frame(window)
loginFrame.place(x=550,y=150)
logoImg=ImageTk.PhotoImage(file="newlogo2.jpg")
logolabel=Label(loginFrame,image=logoImg)
logolabel.image=logoImg
logolabel.grid(row=0,column=0)
window.mainloop()
#hi