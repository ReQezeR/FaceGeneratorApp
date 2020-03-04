import os
import sys
import tkinter as tk
from tkinter import font as tkfont

from DatabaseFrontend.MenuPage import Menu
from DatabaseFrontend.DatabasePage import DatabasePage
from DatabaseFrontend.GeneratorPage import GeneratorPage
from DatabaseBackend.Backend import DbProvider


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.database = DbProvider()
        self.t1 = None
        self.title_font = tkfont.Font(family='Helvetica', size=40, weight="bold", slant="italic")
        self.sizeFlag = False
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, DatabasePage, GeneratorPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def exit_callback(self):
        try:
            self.t1.kill()
            self.t1.join()
        except:
            print("thread exit error")
        self.destroy()

    def make_window_bigger(self):
        self.geometry('1300x650')
        self.minsize(1300, 650)

    def make_window_smaller(self):
        self.geometry('440x650')
        self.minsize(440, 650)

    def show_frame(self, page_name):
        #  Show a frame for the given page name
        if page_name != "Menu" and self.sizeFlag == False:
            self.make_window_bigger()
            self.sizeFlag = True
        elif page_name == "Menu" and self.sizeFlag == True:
            self.make_window_smaller()
            self.sizeFlag = False

        frame = self.frames[page_name]
        frame.tkraise()

    # path to files include in exe
    def resource_path(self, relative_path):
        default = "Frontend/Images/"
        relative_path = default + relative_path
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("..")
        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = App()
    app.wm_protocol("WM_DELETE_WINDOW", app.exit_callback)
    app.minsize(440, 650)
    app.title("Database Client")
    app.geometry("440x650")
    app.mainloop()
