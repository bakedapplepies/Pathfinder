import os

import tkinter
from tkinter import Frame, Label, Button
from PIL import Image, ImageTk


class GUIControl(tkinter.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pathfinder Controls")
        icon = Image.open("resources/icons/32_pathfinder_icon.png")
        photo = ImageTk.PhotoImage(icon)
        self.wm_iconphoto(False, photo)
        # self.embed = Frame(self, width=300, height=300)
        # self.embed.pack()
        # os.environ["SDL_WINDOWID"] = str(self.embed.winfo_id())
        # os.environ["SDL_VIDEODRIVER"] = "windib"
        self.button1 = Button(self, text="click me", command=self.addNumber)
        self.frame = Frame(self, width=300, height=200)
        self.num = 0
        self.label1 = Label(self, text=self.num)
        self.frame.pack()
        self.button1.pack()
        self.label1.pack()
        self.update()
        # self.mainloop()
        # self.update()
        
    def addNumber(self):
        self.num += 1
        