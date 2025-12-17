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
