import tkinter as tk
from tkinter import font as tkfont

from PIL import Image, ImageTk
from pandastable import Table, pd


class CustomOptionMenu(tk.OptionMenu):
    def __init__(self, master, status, *options):
        tk.OptionMenu.__init__(self, master, status, *options)
        self.config(font=('calibri',(10)),bg='white',width=12)
        self['menu'].config(font=('calibri',(10)),bg='white')
        self.status = status

    def get(self):
        return self.status.get()


class DatabasePage(tk.Frame):
    def setTheme(self, bg):
        self.backgroundColor = "white"
        self.secondBackgroundColor = bg
        self.testColor = "orange"
        self.white = "#FFFFFF"
        self.table_ifont = tkfont.Font(family='Helvetica', size=20, slant="roman")
        self.table_nfont = tkfont.Font(family='Helvetica', size=20)
        self.Table_font = tkfont.Font(family='Helvetica', size=20, weight="bold", slant="italic")
        self.databaseLabel = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\DatabasePage\\databaseMenuLabel.png")))
        self.generatorMenuButton = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\MenuPage\\generatorButtonImage.png")))
        self.helpMenuButton = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\MenuPage\\helpButtonImage.png")))
        self.customButtonImage = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\defaultButtonImage.png")))
        self.menuLabelImage = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\MenuPage\\menuLabelImage.png")))
        self.returnButtonImage = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\returnButton.png")))
        self.getDataButton = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\DatabasePage\\showDataButton.png")))
        self.insertDataButton = ImageTk.PhotoImage(Image.open(self.controller.resource_path("Images\\DatabasePage\\insertDataButton.png")))

    def createMenu(self, parent):
        main_frame = tk.Frame(parent, borderwidth=20, background="#FFFFFF")
        tk.Label(main_frame, text='Database', image=self.databaseLabel, font=self.button_font, bg="#FFFFFF").pack(fill=tk.BOTH, expand=1)
        self.createSpace(main_frame, 30).pack(fill=tk.BOTH, expand=1)
        self.customButton(main_frame, "Mode", self.insertDataButton, lambda: self.toggleMode(),
                          x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9", toggle=1).pack(expand=0)
        self.createSpace(main_frame, 250).pack(fill=tk.BOTH, expand=1)
        self.customButton(main_frame, "Return", self.returnButtonImage, lambda: self.controller.show_frame("Menu"), x=self.x / 2, xmargin=10, bgcolor="#666666", fontcolor="#8BB0F9").pack(expand=0)

        self.createSpace(main_frame, 30).pack(fill=tk.BOTH, expand=1)
        return main_frame

    def toggleMode(self):
        if self.mode == 1:
            self.mode = 2
            self.frames['data'].tkraise()
            self.toggleButton['image'] = self.insertDataButton
        elif self.mode == 2:
            self.mode = 1
            self.frames['input'].tkraise()
            self.toggleButton['image'] = self.getDataButton


    def createSpace(self, parent, y):
        temp_frame = tk.LabelFrame(parent, bd=0, bg="white", height=y)
        temp_frame.pack(fill=tk.BOTH, expand=0)
        return temp_frame

    def customButton(self, parent, text, img, cmd, x=10, y=1, xmargin=0, ymargin=0, bgcolor="#FFA900", fontcolor="#FFFFFF", toggle=0):
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
                           command=cmd)
        if (toggle == 1):
            self.toggleButton = button
        button.pack(expand=1)

        temp_label_2 = tk.Label(main_frame, width=int(x / 7), height=int(ymargin / 2), bg=self.white)  # add space
        temp_label_2.pack()
        return main_frame

    def featureEntry(self, parent):
        eyes_colors = ["blue", "green", "black", "brown"]
        skin_types = ["white", "black"]
        colours = ["bright", "dark"]
        hair_type = ["long", "short"]
        sizes = ["small", "medium", "large"]

        cell_width = 1
        px = 5
        ipx = 2
        py = 1
        txt = tk.StringVar()
        txt.set("PLACEHOLDER")

        dataFrame = tk.Frame(parent, width=430, bd=0, bg="white")
        dataFrame.columnconfigure(0, weight=2)
        dataFrame.columnconfigure(1, weight=1)
        dataFrame.columnconfigure(2, weight=1)
        dataFrame.columnconfigure(3, weight=1)
        dataFrame.rowconfigure(0, weight=1)
        dataFrame.rowconfigure(1, weight=1)
        dataFrame.rowconfigure(2, weight=1)
        dataFrame.rowconfigure(3, weight=1)
        dataFrame.rowconfigure(4, weight=1)
        dataFrame.rowconfigure(5, weight=1)
        dataFrame.rowconfigure(6, weight=1)
        dataFrame.rowconfigure(7, weight=1)

        self.l[0] = tk.Label(dataFrame, text="Face:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[0].grid(row=0, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[1] = tk.Label(dataFrame, text="Hair:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[1].grid(row=1, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[2] = tk.Label(dataFrame, text="Eyes:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[2].grid(row=2, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[3] = tk.Label(dataFrame, text="EyeBrows:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[3].grid(row=3, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[4] = tk.Label(dataFrame, text="Nose:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[4].grid(row=4, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[5] = tk.Label(dataFrame, text="Mouth:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[5].grid(row=5, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[6] = tk.Label(dataFrame, text="Ears:", anchor="w", font=self.table_ifont, width=cell_width, bd=0,
                             relief="solid", bg="white")
        self.l[6].grid(row=6, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        cell_width = 8

        def faceEntry(row_nr):      # db.addFace("white", "small", "InputFace-01")
            feature = [i for i in range(3)]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            feature[1] = CustomOptionMenu(dataFrame, tk.StringVar(value="SkinType"), *skin_types)
            feature[1].grid(row=row_nr, column=2, pady=py, padx=px, sticky="ew")
            feature[2] = tk.Entry(dataFrame, textvariable= tk.StringVar(value="Dictionary"), bd=2, font=self.table_nfont, width=cell_width)
            feature[2].grid(row=row_nr, column=3, pady=py, padx=px, sticky="ew")
            return feature

        def eyesEntry(row_nr):      # db.addEyes("small", "blue", "white", "InputFace-01")
            feature = [i for i in range(2)]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Colour"), *eyes_colors)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            feature[1] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[1].grid(row=row_nr, column=2, pady=py, padx=px, sticky="ew")
            return feature

        def earsEntry(row_nr):      # db.addEars("small", "white", "InputFace-01")
            feature = [i for i in range(2)]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            return feature

        def eyeBrowsEntry(row_nr):  # db.addEyeBrows("small", "bright", "white", "InputFace-01")
            feature = [i for i in range(2)]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Colour"), *colours)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            feature[1] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[1].grid(row=row_nr, column=2, pady=py, padx=px, sticky="ew")
            return feature

        def noseEntry(row_nr):      # db.addNose("small", "white", "InputFace-01")
            feature = [0]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            return feature

        def mouthEntry(row_nr):      # db.addMouth("small", "white", "InputFace-01")
            feature = [0]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Size"), *sizes)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            return feature

        def hairEntry(row_nr):     # db.addHair("long", "bright", "white", "InputFace-01")
            feature = [i for i in range(2)]
            feature[0] = CustomOptionMenu(dataFrame, tk.StringVar(value="Type"), *hair_type)
            feature[0].grid(row=row_nr, column=1, pady=py, padx=px, sticky="ew")
            feature[1] = CustomOptionMenu(dataFrame, tk.StringVar(value="Colour"), *colours)
            feature[1].grid(row=row_nr, column=2, pady=py, padx=px, sticky="ew")
            return feature

        self.features[0] = faceEntry(0)
        self.features[1] = hairEntry(1)
        self.features[2] = eyesEntry(2)
        self.features[3] = eyeBrowsEntry(3)
        self.features[4] = noseEntry(4)
        self.features[5] = mouthEntry(5)
        self.features[6] = earsEntry(6)
        return dataFrame

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

        self.table = Table(field, dataframe=df, showtoolbar=False, showstatusbar=False)
        self.table.show()
        return field

    def enterCallback(self, event):
        if event.keycode == 13:
            self.callback()

    def callback(self):
        for typ, n in self.names.items():
            query = str(n.get())
            if query.__len__() > 3:
                self.dataSet = self.controller.database.get_data_from_table(str(n.get()))  # wczytanie nowych danych
                self.custom_table.destroy()  # usunięcie starej tabeli
                self.custom_table = self.customPandasTable(self.data_frame)  # stworzenie nowej z aktualnymi danymi
                self.custom_table.pack(fill=tk.BOTH, expand=1)  # rozmieszczenie

    def insert_data(self):
        #TODO: add asserting method to check that all values are correct
        self.controller.database.addEyes(self.features[2][1].get(), self.features[2][0].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addEars(self.features[6][0].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addEyeBrows(self.features[3][1].get(), self.features[3][0].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addNose(self.features[4][0].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addMouth(self.features[5][0].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addHair(self.features[1][0].get(), self.features[1][1].get(), self.features[0][1].get(), self.features[0][2].get())
        self.controller.database.addFace(self.features[0][1].get(), self.features[0][0].get(), self.features[0][2].get())

    def createUpdateBar(self, parent):
        updateFrame = tk.Frame(parent, width=30, bd=0, bg="white", highlightbackground="white", pady=10, padx=20)
        tk.Button(updateFrame, text="INSERT", command=self.insert_data, bg="#FFFFFF", width=30, height=3).pack(expand=1, fill=tk.BOTH)
        return updateFrame

    def createEntry(self, parent, temp_width=50, labelName="wartosc"):
        def createButton(sparent, cont):
            button = tk.Button(cont, text="GET", command=sparent.callback, bg="#666666", width=10)
            return button

        entryFrame = tk.Frame(parent, width=30, bd=0, bg="white", highlightbackground="white", pady=10)
        for i in range(4):
            entryFrame.columnconfigure(i, weight=1)

        createButton(self, entryFrame).pack(expand=0, side=tk.RIGHT)

        def clearBox(event):
            if username.get() == "give name of the table:":
                name.delete(0, 'end')

        username = tk.StringVar()
        username.set("give name of the table:")
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

        self.d = [tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""),
                  tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text="")]
        self.l = [tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""),
                  tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text="")]
        self.features = [[] for i in range(7)]

        self.mode = 2

        self.main_frame = tk.Frame(self, borderwidth=0, relief=tk.GROOVE, background="white")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.input_frame = tk.Frame(self.main_frame, borderwidth=2, relief=tk.GROOVE, background="white")
        self.customEntry = self.featureEntry(self.input_frame)
        self.customEntry.pack(fill=tk.BOTH, expand=1)
        self.bottomBar = self.createUpdateBar(self.input_frame)
        self.bottomBar.pack(fill=tk.BOTH, expand=0)

        self.data_frame = tk.Frame(self.main_frame, borderwidth=2, relief=tk.GROOVE, background="white")
        self.names = {}
        self.entry = self.createEntry(self.data_frame)
        self.entry.pack(fill=tk.BOTH, expand=0)
        self.custom_table = self.customPandasTable(self.data_frame)
        self.custom_table.pack(fill=tk.BOTH, expand=1)

        self.frames = {}
        self.frames['data'] = self.data_frame
        self.frames['input'] = self.input_frame

        self.frames['input'].grid(row=0, column=0, sticky="nsew")
        self.frames['data'].grid(row=0, column=0, sticky="nsew")

        self.main_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

        content_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE, background="white")
        self.createMenu(content_frame).pack(fill=tk.Y, expand=0)

        content_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
