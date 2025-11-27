from tkinter import *
from PIL import ImageTk
window=Tk()

window.geometry("1280x700+0+0")
window.backgroundImage=ImageTk.PhotoImage(file="loginNew1.png")
bglabel=Label(window,image=window.backgroundImage)
bglabel.place(x=0,y=0)

loginFrame=Frame(window)
window.mainloop()
