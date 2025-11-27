from tkinter import *
from PIL import ImageTk
window=Tk()

<<<<<<< HEAD
window.geometry("1740x700+0+0")
window.backgroundImage=ImageTk.PhotoImage(file="loginbg.png")
=======
window.geometry("1280x700+0+0")
window.backgroundImage=ImageTk.PhotoImage(file="loginNew1.png")
>>>>>>> 595e27e1a967d79d055b6835461902d9f274ba43
bglabel=Label(window,image=window.backgroundImage)
bglabel.place(x=0,y=0)

loginFrame=Frame(window)
<<<<<<< HEAD
loginFrame.place(x=550,y=150)
logoImg=ImageTk.PhotoImage(file="newlogo2.jpg")
logolabel=Label(loginFrame,image=logoImg)
logolabel.image=logoImg
logolabel.grid(row=0,column=0)
window.mainloop()
=======
window.mainloop()
>>>>>>> 595e27e1a967d79d055b6835461902d9f274ba43
