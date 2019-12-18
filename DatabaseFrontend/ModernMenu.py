import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image, ImageTk


class Menu(tk.Frame):
    def setTheme(self, bg):
        self.backgroundColor = "white"
        self.secondBackgroundColor = bg
        self.testColor = "orange"
        self.white = "#FFFFFF"
        self.Table_font = tkfont.Font(family='Helvetica', size=20, weight="bold", slant="italic")
        self.databaseMenuButton = ImageTk.PhotoImage(Image.open("Images/MenuPage/databaseButtonImage.png"))
        self.generatorMenuButton = ImageTk.PhotoImage(Image.open("Images/MenuPage/generatorButtonImage.png"))
        self.helpMenuButton = ImageTk.PhotoImage(Image.open("Images/MenuPage/helpButtonImage.png"))
        self.customButtonImage = ImageTk.PhotoImage(Image.open("Images/defaultButtonImage.png"))
        self.menuLabelImage = ImageTk.PhotoImage(Image.open("Images/MenuPage/menuLabelImage.png"))

    def createMenu(self, parent):
        main_frame = tk.Frame(parent, borderwidth=20, background="#FFFFFF")
        tk.Label(main_frame, text='MENU:', image=self.menuLabelImage, font=self.button_font, bg="#FFFFFF").pack(fill=tk.BOTH)
        self.createSpace(main_frame, 80).pack(fill=tk.BOTH, expand=1)
        self.customButton(main_frame, "Baza Danych", self.databaseMenuButton, "DatabasePage", x=self.x/2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        # self.createSpace(main_frame, 30).pack(fill=tk.BOTH, expand=1)
        self.customButton(main_frame, "Generator", self.generatorMenuButton, "GeneratorPage", x=self.x/2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        self.createSpace(main_frame, 80).pack(fill=tk.BOTH, expand=1)
        self.helpButton(main_frame, "Creditsy", self.helpMenuButton, x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        self.createSpace(main_frame, 30).pack(fill=tk.BOTH, expand=1)
        return main_frame

    def createSpace(self, parent, y):
        temp_frame = tk.LabelFrame(parent, bd=0, bg="white", height=y)
        temp_frame.pack(fill=tk.BOTH, expand=0)
        return temp_frame

    def customButton(self, parent, text, img, frame="Menu", x=10, y=1, xmargin=0, ymargin=0, bgcolor="#FFA900", fontcolor="#FFFFFF"):
        main_frame = tk.LabelFrame(parent, bd=0, bg=self.secondBackgroundColor, width=x, height=y)
        main_frame.pack(fill=tk.BOTH, expand=0)

        tk.Grid.rowconfigure(main_frame, 0, weight=1)
        tk.Grid.columnconfigure(main_frame, 0, weight=1)

        temp_label_1 = tk.Label(main_frame, width=int(x / 7), height=int(ymargin / 2), bg=self.white)  # add space

        temp_label_1.pack()
        button = tk.Button(main_frame,
                           text=text,
                           font=self.button_font,
                           padx=10,
                           pady=10,
                           bd=0,
                           image=img,
                           bg=bgcolor,
                           fg=fontcolor,
                           command=lambda: self.controller.show_frame(frame))
        button.pack(expand=1)

        temp_label_2 = tk.Label(main_frame, width=int(x / 7), height=int(ymargin / 2), bg=self.white)  # add space
        temp_label_2.pack()
        return main_frame

    def helpButton(self, parent, text, img, x=10, y=1, xmargin=0, ymargin=0, bgcolor="#FFA900", fontcolor="#FFFFFF"):
        def clicked():
            messagebox.showinfo('HELP', 'Aplikacja do obsługi bazy danych.')
        main_frame = tk.LabelFrame(parent, bd=0, bg=self.secondBackgroundColor, width=x, height=y)
        main_frame.pack(fill=tk.BOTH, expand=0)

        tk.Grid.rowconfigure(main_frame, 0, weight=1)
        tk.Grid.columnconfigure(main_frame, 0, weight=1)

        temp_label_1 = tk.Label(main_frame, width=int(x / 7), height=int(ymargin / 2), bg=self.white)  # add space

        temp_label_1.pack()
        button = tk.Button(main_frame,
                           text=text,
                           font=self.button_font,
                           padx=10,
                           pady=10,
                           bd=0,
                           image=img,
                           bg=bgcolor,
                           fg=fontcolor,
                           command=lambda: clicked())
        button.pack(expand=1)

        temp_label_2 = tk.Label(main_frame, width=int(x / 7), height=int(ymargin / 2), bg=self.white)  # add space
        temp_label_2.pack()
        return main_frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=200)
        self.controller = controller
        self.parent = parent
        # self.setColors("#110E0A")
        self.setTheme("#FFFFFF")

        self.configure(bg=self.backgroundColor)
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold", slant="italic")

        self.x = self.winfo_reqwidth()
        self.y = self.winfo_reqheight()

        pad_frame = tk.Frame(self, borderwidth=2, background="gray75")
        pad_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=15)

        content_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.createMenu(content_frame).pack(fill=tk.Y, expand=0)

        content_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
