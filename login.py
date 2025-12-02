from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#Checks if the username and password entered is correct or not
# def login() : 
#     if 

window = Tk()
window.geometry("1280x700+0+0")
window.title("Student Management System")
bg_img = Image.open("loginNew1.png")
bg_img = bg_img.resize((1280, 700))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

loginFrame = Frame(
    window,
    bg="white",
    width=380,
    height=500,
    highlightbackground="#4a90e2",
    highlightthickness=3,
    highlightcolor="#4a90e2"
)
loginFrame.place(x=850, y=120)

# TITLE
Label(loginFrame, text="LOGIN HERE",fg= "#002147", font=("Times New Roman", 24, "bold"), bg="white").place(x=80, y=30)

# USERNAME
username_label=Label(loginFrame, text="Username:",fg= "DodgerBlue4", font=("Cascadia code", 14), bg="white").place(x=40, y=120)
usename_entry=Entry(loginFrame, font=("Arial", 14), width=25).place(x=40, y=150)

# PASSWORD
password_label=Label(loginFrame, text="Password:",fg= "DodgerBlue4", font=("Cascadia code", 14), bg="white").place(x=40, y=220)
password_entry=Entry(loginFrame, font=("Arial", 14), width=25, show="*").place(x=40, y=250)

# LOGIN BUTTON
Button(loginFrame, text="Login", font=("Arial", 16, "bold"), width=12,
       bg="#4a90e2", fg="white", relief=FLAT).place(x=110, y=330)

window.mainloop()