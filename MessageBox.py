import tkinter
import os
from tkinter import *
import tkinter.messagebox
class MessageBox(object):

    def __init__(self, msg, b1, b2, t, entry):

        root = self.root = tkinter.Tk()
        root.title('')
        photo = PhotoImage(file='triqui.png')
        root.iconphoto(False,photo)
        self.msg = str(msg)
        root.bind('<Control-c>', func=self.to_clip)
        # buttons
        self.b1_return = True
        self.b2_return = False
        if isinstance(b1, tuple): b1, self.b1_return = b1
        if isinstance(b2, tuple): b2, self.b2_return = b2
        # main frame
        frm_1 = tkinter.Frame(root)
        frm_1.pack(ipadx=2, ipady=2)
        # the message
        message = tkinter.Label(frm_1, text=self.msg)
        message.pack(padx=8, pady=8)
        # if entry=True create and set focus
        if entry:
            self.entry = tkinter.Entry(frm_1)
            self.entry.pack()
            self.entry.focus_set()
        # button frame
        frm_2 = tkinter.Frame(frm_1)
        frm_2.pack(padx=4, pady=4)
        # buttons
        btn_1 = tkinter.Button(frm_2, width=8, text=b1)
        btn_1['command'] = self.b1_action
        btn_1.pack(side='left')
        if not entry: btn_1.focus_set()
        btn_2 = tkinter.Button(frm_2, width=8, text=b2)
        btn_2['command'] = self.b2_action
        btn_2.pack(side='left')

        btn_1.bind('<KeyPress-Return>', func=self.b1_action)
        btn_2.bind('<KeyPress-Return>', func=self.b2_action)

        root.update_idletasks()
        root.eval('tk::PlaceWindow . center')
        # call self.close_mod when the close button is pressed
        root.protocol("WM_DELETE_WINDOW", self.close_mod)

        # if t is specified: call time_out after t seconds
        if t: root.after(int(t*1000), func=self.time_out)

    def b1_action(self, event=None):
        try: x = self.entry.get()
        except AttributeError:
            self.returning = self.b1_return
            self.root.quit()
        else:
            if x:
                self.returning = x
                self.root.quit()

    def b2_action(self, event=None):
        self.returning = self.b2_return
        self.root.quit()


    def close_mod(self):
        pass

    def time_out(self):
        try: x = self.entry.get()
        except AttributeError: self.returning = None
        else: self.returning = x
        finally: self.root.quit()

    def to_clip(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.msg)