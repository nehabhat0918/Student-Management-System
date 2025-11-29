import tkinter as tk
import time
from tkinter import ttk,Frame,Label,Button,PhotoImage
from ttkthemes import ThemedTk
from tkinter import Frame


count=0
text=''

def slider():
    global text,count
    if count<len(s):

        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
        sliderLabel.after(300,slider)

def clock():
    date=time.strftime("%d/%m/%Y")
    current_time=time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f" Date:{date}\nTime: {current_time}")
    datetimeLabel.after(1000,clock)
                         

window=ThemedTk(theme="scidblue")


#mobile=tk.StringVar()
window.geometry('1174x680+50+20')
window.resizable(0,0)

window.title("Student Management System")
mobile=tk.StringVar()
datetimeLabel=tk.Label(window,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=tk.Label(window,text=s,font=('arial',28,'bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

#window=ThemedTk(theme="scidblue")

connect_Button=ttk.Button(window,text='Connect database')
connect_Button.place(x=980,y=0)


leftFrame=Frame(window,bg='green')
leftFrame.place(x=58,y=80,width=300,height=600)

logo_image=tk.PhotoImage(file="std.png")
logo_Label=tk.Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)
import tkinter as tk
import time
from tkinter import ttk,Frame,Label,Button,PhotoImage
from ttkthemes import ThemedTk
from tkinter import Frame
from tkinter import Scrollbar,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,X,Y


count=0
text=''

def slider():
    global text,count
    if count<len(s):

        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
        sliderLabel.after(300,slider)

def clock():
    date=time.strftime("%d/%m/%Y")
    current_time=time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f" Date:{date}\nTime: {current_time}")
    datetimeLabel.after(1000,clock)
                         

window=ThemedTk(theme="scidblue")


#mobile=tk.StringVar()
window.geometry('1174x680+50+20')
window.resizable(0,0)

window.title("Student Management System")
mobile=tk.StringVar()
datetimeLabel=tk.Label(window,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=tk.Label(window,text=s,font=('arial',28,'bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

#window=ThemedTk(theme="scidblue")

connect_Button=ttk.Button(window,text='Connect database')
connect_Button.place(x=980,y=0)


leftFrame=Frame(window,bg='green')
leftFrame.place(x=58,y=80,width=300,height=600)

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

rightFrame=Frame(window,bd=10,bg='white')
rightFrame.place(x=350,y=80,height=820)

tableFrame=Frame(rightFrame,bg='white')
tableFrame.pack(fill=tk.BOTH,expand=1)


scrollBarX=Scrollbar(tableFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(tableFrame,orient=VERTICAL)

studentTable=ttk.Treeview(tableFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'))
studentTable.configure(xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set,show='headings')

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=tk.X)
scrollBarY.pack(side=RIGHT,fill=tk.Y)

studentTable.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.config(show='headings')

window.mainloop()