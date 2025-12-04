import tkinter as tk
import time
from tkinter import ttk,Frame,Label,Button,PhotoImage
from ttkthemes import ThemedTk
from tkinter import Frame
from tkinter import Scrollbar,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,X,Y

import tkinter as tk
import time
from tkinter import ttk
from ttkthemes import ThemedTk

count = 0
text = ""
s = "Student Management System"

# Smooth slider animation
def slider():
    global text, count

    # Reset when completed
    if count >= len(s):
        text = ""
        count = 0
        sliderLabel.config(text="")
        sliderLabel.after(800, slider)   # Pause before restarting
        return

    # Add one character at a time
    text += s[count]
    sliderLabel.config(text=text)

    count += 1

    sliderLabel.after(150, slider)

# Digital clock
def clock():
    date = time.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f"Date: {date}\nTime: {current_time}")
    datetimeLabel.after(1000, clock)

# Window
window = ThemedTk(theme="breeze")
window.geometry("1174x680+50+20")
window.title("Student Management System")
window.configure(bg="#dcdcdc")   # Dark blue background

# Date & Time Label
datetimeLabel = tk.Label(
    window,
    text="",
    font=('Times New Roman', 18, 'bold'),
    bg="#dcdcdc",
    fg="#0F172A"
)
datetimeLabel.place(x=28, y=5)
clock()

# Slider Label
sliderLabel = tk.Label(
    window,
    text="",
    fg="#0F172A",
    bg="#dcdcdc",
    font=("Times New Roman", 28, "bold"),
    width=30
)
sliderLabel.place(x=350, y=10)

slider()

connect_Button=ttk.Button(window,text='Connect database')
connect_Button.place(x=1100,y=15)

leftFrame=Frame(window,bg='midnightblue')
leftFrame.place(x=30,y=80,width=300,height=600)

logo_image=tk.PhotoImage(file="std.png")
logo_Label=tk.Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

add_student_Button=tk.Button(leftFrame,text='Add Student',width=25)
add_student_Button.grid(row=2,column=2,pady=20)

search_student_Button=tk.Button(leftFrame,text='Search Student',width=25)
search_student_Button.grid(row=4,column=2,pady=20)

delete_student_Button=tk.Button(leftFrame,text='Delete Student',width=25)
delete_student_Button.grid(row=6,column=2,pady=20)

update_student_Button=tk.Button(leftFrame,text='Update Student',width=25)
update_student_Button.grid(row=8,column=2,pady=20)

show_student_Button=tk.Button(leftFrame,text='Show Student',width=25)
show_student_Button.grid(row=10,column=2,pady=20)

export_student_Button=tk.Button(leftFrame,text='Export data',width=25)
export_student_Button.grid(row=12,column=2,pady=20)

exit_student_Button=tk.Button(leftFrame,text='Exit',width=25)
exit_student_Button.grid(row=14,column=2,pady=20)

rightFrame=Frame(window,bd=10,bg='white',padx=-20)
rightFrame.place(x=350,y=80,height=600)

tableFrame = Frame(rightFrame, bg="white")
tableFrame.pack(fill=tk.BOTH, expand=True)

scrollBarY = Scrollbar(tableFrame, orient=VERTICAL)

studentTable = ttk.Treeview(
    tableFrame,
    columns=("Id","Name","D.O.B","Gender","Mobile No.","Email"),
    show="headings",
    yscrollcommand=scrollBarY.set
)

scrollBarY.config(command=studentTable.yview)

scrollBarY.pack(side=RIGHT, fill=Y)
studentTable.pack(fill=tk.BOTH, expand=True)

studentTable.pack(fill=tk.BOTH, expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Mobile No.',text='Mobile No.')
studentTable.heading('Email',text='Email Id')

studentTable.column('Id', width=100, anchor="center")
studentTable.column('Name', width=120, anchor="center")
studentTable.column('D.O.B', width=70, anchor="center")
studentTable.column('Gender', width=150, anchor="center")
studentTable.column('Mobile No.', width=200, anchor="center")
studentTable.column('Email', width=200, anchor="center")

#dummy details
for i in range(1,10):
    studentTable.insert("", "end",
                        values=(i, f"Name{i}", "01/01/2000", "Male",
                                "9876543210", f"user{i}@mail.com"))

studentTable.config(show='headings')

window.mainloop()