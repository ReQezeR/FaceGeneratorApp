import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image, ImageTk
import tkintertable as tktable
from DatabaseFrontend.CustomCanvasTable import CustomCanvas


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

    def customTkTable(self, parent):
        field = tk.LabelFrame(parent, bd=0, bg="#515E5A")
        field.pack(fill=tk.Y, expand=1)

        self.table = tktable.TableCanvas(field, data=self.dataSet, bg="#000000", insertbackground="black", selectbackground="white")
        self.table.cellbackgr = "#FFFFFF"
        self.table.multipleselectioncolor = "#FFFFFF"
        self.table.rowselectedcolor = "#8BB0F9"
        self.table.selectedcolor = "#2B20FF"
        self.table.grid_color = "#FFFFFF"

        CustomCanvas(self.table).adjustColumnWidths()
        self.table.show()
        return field

    def callback(self):
        for typ, n in self.names.items():
            self.dataSet = self.controller.database.get_data_from_table(str(n.get())) # wczytanie nowych danych
            self.custom_table.destroy()  # usunięcie starej tabeli
            self.custom_table = self.customTkTable(self.input_frame)  # stworzenie nowej z aktualnymi danymi
            self.custom_table.pack(fill=tk.BOTH, expand=1)  # rozmieszczenie

    def createButton(self, cont):
        button = tk.Button(cont, text="GET", command=self.callback, bg="#666666", width=10)
        return button

    def createEntry(self, parent, temp_width=50, labelName="wartosc"):
        dataFrame = tk.Frame(parent, width=30, bd=0, bg="white")
        dataFrame.columnconfigure(0, weight=1)
        dataFrame.columnconfigure(1, weight=1)
        dataFrame.columnconfigure(2, weight=1)
        dataFrame.columnconfigure(3, weight=1)
        self.createButton(dataFrame).grid(row=0, column=2)

        def clearBox(self):
            name.delete(0, 'end')
        username = tk.StringVar()
        username.set("podaj nazwe tabeli: ")
        name = tk.Entry(dataFrame, bd=2, textvariable=username, width=temp_width)
        name.bind('<Button-1>', clearBox)
        name.grid(row=0, column=1)
        self.names[labelName] = name
        return dataFrame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=200)
        self.controller = controller
        self.parent = parent
        # self.setColors("#110E0A")
        self.dataSet = controller.database.get_data_from_table("CustomFace")
        self.setTheme("#FFFFFF")

        self.configure(bg=self.backgroundColor)
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold", slant="italic")

        self.x = self.winfo_reqwidth()
        self.y = self.winfo_reqheight()

        self.input_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.names = {}
        self.entry = self.createEntry(self.input_frame)
        self.entry.pack(fill=tk.BOTH, expand=0)
        self.custom_table = self.customTkTable(self.input_frame)
        self.custom_table.pack(fill=tk.BOTH, expand=1)

        self.input_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

        content_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.createMenu(content_frame).pack(fill=tk.Y, expand=0)

        content_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
