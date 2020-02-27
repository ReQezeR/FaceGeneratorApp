import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

from PIL import Image, ImageTk
from pandastable import Table, pd


class DatabasePage(tk.Frame):
    def setTheme(self, bg):
        self.backgroundColor = "white"
        self.secondBackgroundColor = bg
        self.testColor = "orange"
        self.white = "#FFFFFF"
        self.Table_font = tkfont.Font(family='Helvetica', size=20, weight="bold", slant="italic")
        self.databaseLabel = ImageTk.PhotoImage(Image.open("Images/DatabasePage/databaseMenuLabel.png"))
        self.generatorMenuButton = ImageTk.PhotoImage(Image.open("Images/MenuPage/generatorButtonImage.png"))
        self.helpMenuButton = ImageTk.PhotoImage(Image.open("Images/MenuPage/helpButtonImage.png"))
        self.customButtonImage = ImageTk.PhotoImage(Image.open("Images/defaultButtonImage.png"))
        self.menuLabelImage = ImageTk.PhotoImage(Image.open("Images/MenuPage/menuLabelImage.png"))
        self.returnButtonImage = ImageTk.PhotoImage(Image.open("Images/returnButton.png"))

    def createMenu(self, parent):
        main_frame = tk.Frame(parent, borderwidth=20, background="#FFFFFF")
        tk.Label(main_frame, text='Database', image=self.databaseLabel, font=self.button_font, bg="#FFFFFF").pack(fill=tk.BOTH, expand=1)
        # self.customButton(main_frame, "Cecha 1", self.customButtonImage, "DatabasePage", x=self.x / 4, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        # self.customButton(main_frame, "Cecha 2", self.customButtonImage, "DatabasePage", x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        # self.customButton(main_frame, "Cecha 3", self.customButtonImage, "DatabasePage", x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=False)
        self.customButton(main_frame, "Return", self.returnButtonImage, "Menu", x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=0)

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

    def customPandasTable(self, parent):
        def set_order(cols_order): # fix kolejnosci kolumn
            x = []
            for i in cols_order:
                x.append(list(df.columns).index(i))
            return x

        field = tk.LabelFrame(parent, bd=0, bg="#515E5A")
        field.pack(fill=tk.BOTH, expand=1)

        df = pd.DataFrame(self.dataSet)  # wczytanie danych

        df = df.transpose()  # transpozycja danych ( zamiana wierszy z kolumnami )

        if df.keys().__len__() is not 0:
            df = df[df.columns[set_order(list(self.dataSet[str(0)].keys()))]]

        if 'Result' in df.columns:
            df['AssignmentID'] = df['AssignmentID'].astype(int)
        if 'ID' in df.columns:
            df['ID'] = df['ID'].astype(int)

        print(df['ID'].dtype)

        self.table = Table(field, dataframe=df, showtoolbar=False, showstatusbar=False)
        self.table.show()
        return field

    def enterCallback(self, event):
        if event.keycode == 13:
            self.callback()

    def callback(self):
        for typ, n in self.names.items():
            query = str(n.get())
            print(query)
            if query.__len__() > 3:
                self.dataSet = self.controller.database.get_data_from_table(str(n.get())) # wczytanie nowych danych
                self.custom_table.destroy()  # usunięcie starej tabeli
                self.custom_table = self.customPandasTable(self.input_frame) # stworzenie nowej z aktualnymi danymi
                self.custom_table.pack(fill=tk.BOTH, expand=1)  # rozmieszczenie

    def createButton(self, cont):
        button = tk.Button(cont, text="GET", command=self.callback, bg="#666666", width=10)
        return button

    def createEntry(self, parent, temp_width=50, labelName="wartosc"):
        entryFrame = tk.Frame(parent, width=30, bd=0, bg="white", highlightbackground="white", pady=10)
        for i in range(4):
            entryFrame.columnconfigure(i, weight=1)

        self.createButton(entryFrame).pack(expand=0, side=tk.RIGHT)

        def clearBox(event):
            if username.get() == "podaj nazwe tabeli: ":
                name.delete(0, 'end')

        username = tk.StringVar()
        username.set("podaj nazwe tabeli: ")
        name = tk.Entry(entryFrame, bd=3, textvariable=username, width=temp_width)
        name.bind('<Button-1>', clearBox)
        name.bind("<Key>", self.enterCallback)
        name.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

        self.names[labelName] = name
        return entryFrame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=200)
        self.controller = controller
        self.parent = parent
        # self.setColors("#110E0A")
        self.dataSet = controller.database.get_data_from_table("Appearance")
        self.setTheme("#FFFFFF")

        self.configure(bg=self.backgroundColor)
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold", slant="italic")

        self.x = self.winfo_reqwidth()
        self.y = self.winfo_reqheight()

        self.input_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.names = {}
        self.entry = self.createEntry(self.input_frame)
        self.entry.pack(fill=tk.BOTH, expand=0)
        self.custom_table = self.customPandasTable(self.input_frame)
        self.custom_table.pack(fill=tk.BOTH, expand=1)

        self.input_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

        content_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.createMenu(content_frame).pack(fill=tk.Y, expand=0)

        content_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
