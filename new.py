import wx
import csv
import os
import time

APP_TITLE = "Student Management System (wxPython)"
FILENAME = "students.csv"
S = "Student Management System"


# ---------------------- LOGIN WINDOW ----------------------
class LoginDialog(wx.Dialog):
    def _init_(self, parent):
        super()._init_(parent, title="Login", size=(820, 480))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Optional image
        try:
            img = wx.Image("loginNew1.png").Rescale(400, 240).ConvertToBitmap()
            sizer.Add(wx.StaticBitmap(panel, bitmap=img), 0, wx.ALIGN_CENTER | wx.TOP, 8)
        except:
            pass

        # Username
        sizer.Add(wx.StaticText(panel, label="Username:"), 0, wx.LEFT | wx.TOP, 12)
        self.user_txt = wx.TextCtrl(panel)
        sizer.Add(self.user_txt, 0, wx.EXPAND | wx.ALL, 12)

        # Password
        sizer.Add(wx.StaticText(panel, label="Password:"), 0, wx.LEFT, 12)
        self.pwd_txt = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.pwd_txt, 0, wx.EXPAND | wx.ALL, 12)

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


# ---------------------- ADD / UPDATE STUDENT WINDOW ----------------------
class StudentDialog(wx.Dialog):
    def _init_(self, parent, title="Add Student", data=None):
        super()._init_(parent, title=title, size=(550, 380))
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
