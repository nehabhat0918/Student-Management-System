
import wx
import csv
import os
import time

APP_TITLE = "Student Management System (wxPython)"
FILENAME = "students.csv"
S = "Student Management System"


#LOGIN WINDOW
class LoginDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Login", size=(820, 480))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Optional image
        try:
            img = wx.Image("loginNew1.png").Rescale(400, 240).ConvertToBitmap()
            sizer.Add(wx.StaticBitmap(panel, bitmap=img), 0, wx.ALIGN_CENTER | wx.TOP, 8)
        except:
            pass

       # Username (centered)
        sizer.Add(wx.StaticText(panel, label="Username:"), 0, wx.ALIGN_CENTER | wx.TOP, 12)

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.user_txt = wx.TextCtrl(panel)
        self.user_txt.SetMinSize((250, -1))   # width control
        user_sizer.Add(self.user_txt, 0, wx.ALIGN_CENTER)

        sizer.Add(user_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 8)


        # Password (centered)
        sizer.Add(wx.StaticText(panel, label="Password:"), 0, wx.ALIGN_CENTER | wx.TOP, 12)

        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.pwd_txt = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        self.pwd_txt.SetMinSize((250, -1))
        pwd_sizer.Add(self.pwd_txt, 0, wx.ALIGN_CENTER)

        sizer.Add(pwd_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 8)



        # Buttons
        btn_sizer = wx.StdDialogButtonSizer()
        login_btn = wx.Button(panel, wx.ID_OK, "Login")
        cancel_btn = wx.Button(panel, wx.ID_CANCEL, "Cancel")
        login_btn.SetDefault()

        btn_sizer.AddButton(login_btn)
        btn_sizer.AddButton(cancel_btn)
        btn_sizer.Realize()
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        panel.SetSizer(sizer)

        login_btn.Bind(wx.EVT_BUTTON, self.on_login)

    def on_login(self, event):
        if self.user_txt.GetValue().strip() == "Admin" and self.pwd_txt.GetValue().strip() == "6767":
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Invalid credentials", "Error", wx.ICON_ERROR)


# ADD / UPDATE STUDENT WINDOW
class StudentDialog(wx.Dialog):
    def __init__(self, parent, title="Add Student", data=None):
        super().__init__(parent, title=title, size=(550, 380))
        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Form Grid
        grid = wx.FlexGridSizer(5, 2, 15, 15)
        grid.AddGrowableCol(1, 1)

        labels = ["Name", "D.O.B", "Gender", "Mobile", "Email"]
        self.entries = {}

        for lab in labels:
            lbl = wx.StaticText(panel, label=f"{lab}:")
            txt = wx.TextCtrl(panel, size=(300, 32))  # FIXED HEIGHT & WIDTH
            self.entries[lab] = txt

            grid.Add(lbl, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 15)
            grid.Add(txt, 1, wx.EXPAND | wx.RIGHT, 15)

        main_sizer.Add(grid, 1, wx.ALL | wx.EXPAND, 20)

        # Pre-fill when updating
        if data:
            for i, lab in enumerate(labels, start=1):
                self.entries[lab].SetValue(data[i])

        # Buttons
        btn_box = wx.StdDialogButtonSizer()
        save_btn = wx.Button(panel, wx.ID_OK, "Save")
        cancel_btn = wx.Button(panel, wx.ID_CANCEL, "Cancel")

        btn_box.AddButton(save_btn)
        btn_box.AddButton(cancel_btn)
        btn_box.Realize()

        main_sizer.Add(btn_box, 0, wx.ALIGN_CENTER | wx.ALL, 15)

        panel.SetSizer(main_sizer)
        self.Layout()

    def get_values(self):
        return [
            self.entries["Name"].GetValue(),
            self.entries["D.O.B"].GetValue(),
            self.entries["Gender"].GetValue(),
            self.entries["Mobile"].GetValue(),
            self.entries["Email"].GetValue(),
        ]


# MAIN DASHBOARD WINDOW
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title=APP_TITLE, size=(1300, 420))
        self.panel = wx.Panel(self)

        self.build_ui()
        self.load_data()

        # Clock
        self.timer_clock = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_clock, self.timer_clock)
        self.timer_clock.Start(1000)

    def build_ui(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # LEFT PANEL
        left = wx.BoxSizer(wx.VERTICAL)

        try:
            img = wx.Image("std.png").Rescale(100, 100)
            logo = wx.StaticBitmap(self.panel, bitmap=wx.Bitmap(img))
        except:
            logo = wx.StaticText(self.panel, label="[Logo]")

        left.Add(logo, 0, wx.ALL | wx.ALIGN_CENTER, 12)

        buttons = [
            ("Add Student", self.on_add),
            ("Delete Student", self.on_delete),
            ("Search Student", self.on_search),
            ("Update Student", self.on_update),
            ("Reset", self.on_reset),
            ("Exit", self.on_exit)
        ]

        for text, fn in buttons:
            btn = wx.Button(self.panel, label=text)
            btn.Bind(wx.EVT_BUTTON, fn)
            left.Add(btn, 0, wx.EXPAND | wx.ALL, 8)

        main_sizer.Add(left, 0, wx.ALL, 10)

        # RIGHT PANEL
        right = wx.BoxSizer(wx.VERTICAL)

        # TOP BAR
        top_bar = wx.BoxSizer(wx.HORIZONTAL)

        self.datetime_label = wx.StaticText(self.panel, label="")
        top_bar.Add(self.datetime_label, 0, wx.LEFT | wx.TOP, 8)

        top_bar.AddStretchSpacer()

        # CENTER TITLE
        self.title_label = wx.StaticText(self.panel, label=S, style=wx.ALIGN_CENTER)
        title_font = wx.Font(22, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.title_label.SetFont(title_font)
        top_bar.Add(self.title_label, 0, wx.ALIGN_CENTER | wx.TOP, 5)

        top_bar.AddStretchSpacer()
        right.Add(top_bar, 0, wx.EXPAND)

        # TABLE
        self.list = wx.ListCtrl(self.panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        cols = ["Id", "Name", "D.O.B", "Gender", "Mobile", "Email"]

        for i, c in enumerate(cols):
            self.list.InsertColumn(i, c)

        self.list.SetColumnWidth(0, 60)
        self.list.SetColumnWidth(1, 200)
        self.list.SetColumnWidth(2, 130)
        self.list.SetColumnWidth(3, 110)
        self.list.SetColumnWidth(4, 170)
        self.list.SetColumnWidth(5, 250)

        right.Add(self.list, 1, wx.EXPAND | wx.ALL, 10)
        main_sizer.Add(right, 1, wx.EXPAND)

        self.panel.SetSizer(main_sizer)
        self.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_update)

    #CLOCK
    def update_clock(self, event):
        self.datetime_label.SetLabel(time.strftime("%d/%m/%Y\n%H:%M:%S"))

    #CSV HANDLING
    def load_data(self):
        self.list.DeleteAllItems()
        if os.path.exists(FILENAME):
            with open(FILENAME, newline='', encoding="utf-8") as f:
                for row in csv.reader(f):
                    self.insert_row(row)

    def save_data(self):
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for i in range(self.list.GetItemCount()):
                writer.writerow([
                    self.list.GetItemText(i, col)
                    for col in range(self.list.GetColumnCount())
                ])

    def insert_row(self, row):
        index = self.list.InsertItem(self.list.GetItemCount(), str(row[0]))
        for col in range(1, len(row)):
            self.list.SetItem(index, col, str(row[col]))

    #BUTTON FUNCTIONS
    def on_add(self, event):
        dlg = StudentDialog(self, "Add Student")
        if dlg.ShowModal() == wx.ID_OK:
            vals = dlg.get_values()
            new_id = self.list.GetItemCount() + 1
            self.insert_row([new_id] + vals)
            self.save_data()
        dlg.Destroy()

    def on_delete(self, event):
        sel = self.list.GetFirstSelected()
        if sel == -1:
            wx.MessageBox("Please select a student.", "Warning")
            return

        self.list.DeleteItem(sel)

        # Reassign IDs
        for i in range(self.list.GetItemCount()):
            self.list.SetItem(i, 0, str(i + 1))

        self.save_data()

    def on_update(self, event):
        sel = self.list.GetFirstSelected()
        if sel == -1:
            return

        row = [self.list.GetItemText(sel, col) for col in range(self.list.GetColumnCount())]
        dlg = StudentDialog(self, "Update Student", row)

        if dlg.ShowModal() == wx.ID_OK:
            vals = dlg.get_values()
            for col in range(1, 6):
                self.list.SetItem(sel, col, vals[col - 1])
            self.save_data()

        dlg.Destroy()

    def on_search(self, event):
        dlg = wx.TextEntryDialog(self, "Enter Name / Mobile / Email:", "Search")
        if dlg.ShowModal() == wx.ID_OK:
            key = dlg.GetValue().lower().strip()
            self.load_data()

            remove_ids = []
            for i in range(self.list.GetItemCount()):
                row_data = [self.list.GetItemText(i, col).lower() for col in range(6)]
                if key not in row_data[1] and key not in row_data[4] and key not in row_data[5]:
                    remove_ids.append(i)

            for i in reversed(remove_ids):
                self.list.DeleteItem(i)

        dlg.Destroy()

    def on_reset(self, event):
        self.load_data()

    def on_exit(self, event):
        self.Close()


#APP START 
class MyApp(wx.App):
    def OnInit(self):
        if not os.path.exists(FILENAME):
            open(FILENAME, "w").close()

        login = LoginDialog(None)
        if login.ShowModal() == wx.ID_OK:
            login.Destroy()
            frame = MainFrame()
            frame.Show()
            return True

        login.Destroy()
        return False


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()