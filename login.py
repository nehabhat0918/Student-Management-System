from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#Login button functionality
def login(event=None):
    user = usernameEntry.get().strip()
    pwd = passwordEntry.get().strip()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return

    elif user == "Neha" and pwd == "6767":
        messagebox.showinfo("Success", f"Welcome, {user}!")
    elif user == "Krishnaveni" and pwd == "4567":
        messagebox.showinfo("Success", f"Welcome, {user}!")
    elif user == "Likitha" and pwd == "6789":
        messagebox.showinfo("Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Error", "Please enter correct credentials")

# Main window
window = Tk()
window.geometry("1280x700+0+0")
window.title("Student Management System")
window.resizable(False, False)
bg_img = Image.open("loginNew1.png")
bg_img = bg_img.resize((1280, 700))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Login frame
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

#Title
Label(loginFrame, text="LOGIN HERE", fg="MistyRose4", font=("Times New Roman", 24, "bold"), bg="white").place(x=80, y=30)

# Username
Label(loginFrame, text="Username:", fg="DodgerBlue4", font=("Cascadia Code", 14), bg="white").place(x=40, y=120)
usernameEntry = Entry(loginFrame, font=("Arial", 14), width=25)
usernameEntry.place(x=40, y=150)

# Password
Label(loginFrame, text="Password:", fg="DodgerBlue4", font=("Cascadia Code", 14), bg="white").place(x=40, y=220)
passwordEntry = Entry(loginFrame, font=("Arial", 14), width=25, show="*")
passwordEntry.place(x=40, y=250)

#Login Button
loginButton = Button(loginFrame, text="Login", font=("Arial", 16, "bold"), width=12,
       bg="#4a90e2", fg="white", relief=FLAT, cursor='hand2', command=login)
loginButton.place(x=110, y=330)

window.bind("<Return>", login)
usernameEntry.focus_set()

window.mainloop()