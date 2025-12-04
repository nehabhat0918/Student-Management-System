count = 0
text = ''
def main():
    import tkinter as tk
    import time
    from tkinter import ttk,Frame,Label,Button,PhotoImage
    from ttkthemes import ThemedTk
    from tkinter import Frame
    from tkinter import Scrollbar,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,X,Y

    
    s = 'Student Management System'

    def slider():
        global text, count
        if count < len(s):
            text = text + s[count]
            sliderLabel.config(text=text)
            count += 1
            sliderLabel.after(300, slider)

    def clock():
        date=time.strftime("%d/%m/%Y")
        current_time=time.strftime("%H:%M:%S")
        datetimeLabel.config(text=f" Date:{date}\nTime: {current_time}")
        datetimeLabel.after(1000,clock)

    window=ThemedTk(theme="breeze")


    #mobile=tk.StringVar()
    window.geometry('1174x680+50+20')


    window.title(" Student Management System ")
    mobile=tk.StringVar()
    datetimeLabel=tk.Label(window,text='hello',font=('times new roman',18,'bold'))
    datetimeLabel.place(x=5,y=5)
    clock()
    sliderLabel=tk.Label(window,text=s,font=('Britannic Bold',28),width=30)
    sliderLabel.place(x=400,y=8)
    slider()


    connect_Button=ttk.Button(window,text='Connect database')
    connect_Button.place(x=1350,y=20)

    leftFrame=Frame(window,bg='midnightblue')
    leftFrame.place(x=30,y=80,width=300,height=600)

    logo_image=tk.PhotoImage(file="std.png")
    logo_Label=tk.Label(leftFrame,image=logo_image)
    logo_Label.grid(row=0,column=0)


    #adding functionality
    import csv, os
    from tkinter import messagebox

    FILENAME ="students.csv"

    def load_data():
        if os.path.exists(FILENAME):
            with open(FILENAME, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    studentTable.insert("","end", values=row)

    def save_data():
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row_id in studentTable.get_children():
                row = studentTable.item(row_id)["values"]
                writer.writerow(row)

    def add_student_popup():
        popup = tk.Toplevel(window)
        popup.title("Add Student")
        popup.geometry("400x400")

        tk.Label(popup, text="Name").pack()
        name_entry = tk.Entry(popup)
        name_entry.pack()

        tk.Label(popup, text="DOB").pack()
        dob_entry = tk.Entry(popup)
        dob_entry.pack()

        tk.Label(popup, text="Gender").pack()
        gender_entry = tk.Entry(popup)
        gender_entry.pack()

        tk.Label(popup, text="Mobile").pack()
        mobile_entry = tk.Entry(popup)
        mobile_entry.pack()

        tk.Label(popup, text="Email").pack()
        email_entry = tk.Entry(popup)
        email_entry.pack()

        def save_student():
            new_id = len(studentTable.get_children()) + 1
            new_data = [new_id, name_entry.get(), dob_entry.get(),
                        gender_entry.get(), mobile_entry.get(), email_entry.get()]
            studentTable.insert("", "end", values=new_data)
            save_data()
            messagebox.showinfo("Success", "Student added!")
            popup.destroy()
        tk.Button(popup, text="Save", command=save_student).pack(pady=10)

    def delete_student():
        selected = studentTable.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to delete")
            return
    
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
        if confirm:
            for row in selected:
                studentTable.delete(row)
            save_data()
            messagebox.showinfo("Deleted", "Student deleted successfully!")

    def reset_data():
        # Clear table
        for row in studentTable.get_children():
            studentTable.delete(row)
        # Reload from CSV
        load_data()

    def update_student():
        selected = studentTable.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to update")
            return
    
        row = studentTable.item(selected[0])["values"]
    
        popup = tk.Toplevel(window)
        popup.title("Update Student")
        popup.geometry("400x400")

        tk.Label(popup, text="Name").pack()
        name_entry = tk.Entry(popup)
        name_entry.insert(0, row[1])
        name_entry.pack()

        tk.Label(popup, text="DOB").pack()
        dob_entry = tk.Entry(popup)
        dob_entry.insert(0, row[2])
        dob_entry.pack()

        tk.Label(popup, text="Gender").pack()
        gender_entry = tk.Entry(popup)
        gender_entry.insert(0, row[3])
        gender_entry.pack()

        tk.Label(popup, text="Mobile").pack()
        mobile_entry = tk.Entry(popup)
        mobile_entry.insert(0, row[4])
        mobile_entry.pack()

        tk.Label(popup, text="Email").pack()
        email_entry = tk.Entry(popup)
        email_entry.insert(0, row[5])
        email_entry.pack()

        def save_update():
            updated_data = [
                row[0],  # ID stays same
                name_entry.get(),
                dob_entry.get(),
                gender_entry.get(),
                mobile_entry.get(),
                email_entry.get()
            ]

            studentTable.item(selected[0], values=updated_data)
            save_data()
            messagebox.showinfo("Updated", "Student updated successfully!")
            popup.destroy()

        tk.Button(popup, text="Save Changes", command=save_update).pack(pady=10)

    def search_student():
        popup = tk.Toplevel(window)
        popup.title("Search Student")
        popup.geometry("350x200")

        tk.Label(popup, text="Enter Name / Mobile / Email").pack(pady=10)
        search_entry = tk.Entry(popup, width=30)
        search_entry.pack()

        def perform_search():
            keyword = search_entry.get().lower()

            # Clear table first
            for row in studentTable.get_children():
                studentTable.delete(row)

            # Load and filter
            if os.path.exists(FILENAME):
                with open(FILENAME, newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if (keyword in row[1].lower() or
                            keyword in row[4].lower() or
                            keyword in row[5].lower()):
                            studentTable.insert("", "end", values=row)

            popup.destroy()

        tk.Button(popup, text="Search", command=perform_search).pack(pady=10)

    def exit_app():
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            window.destroy()

    #########################ENDS#########################
    delete_student_Button=tk.Button(leftFrame,text='Delete Student',width=25,command=delete_student)
    delete_student_Button.grid(row=6,column=2,pady=20)


    add_student_Button=tk.Button(leftFrame,text='Add Student',width=25,command=add_student_popup)
    add_student_Button.grid(row=2,column=2,pady=20)

    search_student_Button=tk.Button(leftFrame,text='Search Student',width=25,command=search_student)
    search_student_Button.grid(row=4,column=2,pady=20)

    update_student_Button=tk.Button(leftFrame,text='Update Student',width=25,command=update_student)
    update_student_Button.grid(row=8,column=2,pady=20)

    reset_Button=tk.Button(leftFrame,text='Reset',width=25,command=reset_data)
    reset_Button.grid(row=10,column=2,pady=20)

    exit_student_Button=tk.Button(leftFrame,text='Exit',width=25,command=exit_app)
    exit_student_Button.grid(row=12,column=2,pady=20)

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
    studentTable.pack(fill=tk.BOTH,expand=True)

    studentTable.pack(fill=tk.BOTH,expand=1)

    studentTable.heading('Id', text='Id')
    studentTable.heading('Name', text='Name')
    studentTable.heading('D.O.B', text='D.O.B')
    studentTable.heading('Gender', text='Gender')
    studentTable.heading('Mobile No.', text='Mobile No.')
    studentTable.heading('Email', text='Email Id')

    studentTable.column('Id', width= 100, anchor="center")
    studentTable.column('Name', width= 120, anchor="center")
    studentTable.column('D.O.B', width= 70, anchor="center")
    studentTable.column('Gender', width= 150, anchor="center")
    studentTable.column('Mobile No.', width= 200, anchor="center")
    studentTable.column('Email', width= 200, anchor="center")


    studentTable.config(show='headings')
    load_data()

    window.mainloop()

if __name__=="__main__":
    main()