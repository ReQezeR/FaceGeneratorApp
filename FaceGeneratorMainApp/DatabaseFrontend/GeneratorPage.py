import os
import threading
import tkinter as tk
from datetime import datetime
from tkinter import font as tkfont
from PIL import Image, ImageTk
import cv2
from FaceGeneratorMainApp.DatabaseBackend.Backend import DbProvider
from FaceGeneratorMainApp.DatabaseBackend.ThreadManagement import ThreadWithTrace
from FaceGeneratorMainApp.Generator.Generator import Generator


class GeneratorPage(tk.Frame):
    def file_path(self, relative):
        p = os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)
        return p

    def loadImage(self, path=None):
        size = (500, 400)
        if path != None:
            self.placeholderImage = Image.open(str(path))
        resized = self.placeholderImage.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")

    def resize(self, event):
        # size = (int(590+self.winfo_width() *0.1), int(400 + self.winfo_height()*0.2))
        size = (500, 400)
        resized = self.placeholderImage.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")

    def getXY(self, event):
        self.x = self.winfo_width()
        self.y = self.winfo_height()
        self.update()

    def createHeader(self):
        topFrame = tk.LabelFrame(self, bd=0, bg="white", height=100, width=self.x)
        topFrame.pack(fill=tk.BOTH, expand=1)

        tk.Grid.rowconfigure(topFrame, 0, weight=1)
        tk.Grid.columnconfigure(topFrame, 0, weight=1)
        l0 = tk.Label(topFrame, image=self.generatorTitleImage, bg="white", bd=0, width=300)
        l0.grid(row=0, column=0, sticky="nsew", padx=0, pady=10)

        # tk.Grid.columnconfigure(topFrame, 1, weight=1)
        # l1 = tk.Label(topFrame, text=" ", font=self.table_ifont, bg="white", bd=0, width=10)
        # l1.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        return topFrame

    def changeImage(self, image):
        size = (500, 400)
        self.placeholderImage = image
        resized = cv2.resize(self.placeholderImage, size)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")

    def randomFeatures(self):
         return DbProvider().random_features("white")

    def runGenerator(self):
        self.controller.t1 = ThreadWithTrace(target=self._runGenerator)
        self.controller.t1.start()

    def _runGenerator(self):
        g = Generator()
        temp = self.randomFeatures()
        g.get_files(temp[1])
        g.create_face()
        lock = threading.Lock()
        lock.acquire()
        if not os.path.isdir("Files\\Faces"):
            try:
                os.mkdir(self.file_path("Files\\Faces"))
            except:
                # pass
                print("Nie mozna utworzyc folderu")
        filename = "Face_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+".png"
        path = "Files\\Faces\\"+filename
        DbProvider().appearance.insert_into_table(temp[0], "white", path)
        g.write_face(self.file_path(path))

        lock.release()
        self.changeGenerated()

    def changeData(self):
        self.dataSet = DbProvider().custom_select("SELECT * FROM Appearance ORDER BY ID DESC LIMIT 1;")
        i = 0
        number = 0

        try:
            labels = list(self.dataSet[str(number)].keys())

            for label in labels:
                self.l[i].configure(text=str(label))
                i += 1
            i = 0
            for item in self.dataSet[str(number)]:
                if self.table_version == 1:
                    self.d[i].configure(text=self.dataSet[str(number)][item])
                elif self.table_version == 2:
                    input = tk.StringVar()
                    input.set(str(self.dataSet[str(number)][item]))
                    self.d[i].configure(textvariable=input)
                if i == len(self.dataSet[str(number)]) - 1:
                    self.loadImage(path=self.dataSet[str(number)][item])
                i += 1
        except:
            self.loadImage()

    def changeGenerated(self):
        self.dataSet = DbProvider().custom_select("SELECT * FROM Appearance ORDER BY ID DESC LIMIT 1;")
        i = 0
        number = 0

        labels = list(self.dataSet[str(number)].keys())

        for label in labels:
            self.l[i].configure(text=str(label))
            i += 1
        i = 0
        for item in self.dataSet[str(number)]:
            if self.table_version == 1:
                self.d[i].configure(text=self.dataSet[str(number)][item])
            elif self.table_version == 2:
                input = tk.StringVar()
                input.set(str(self.dataSet[str(number)][item]))
                self.d[i].configure(textvariable=input)
            if i == len(self.dataSet[str(number)]) - 1:
                self.loadImage(path=self.dataSet[str(number)][item])
            i += 1

    def createDataTable(self, parent):
        cell_width = 3
        px = 5
        ipx = 2
        py = 2
        self.table_version = 2
        txt = tk.StringVar()
        txt.set("PLACEHOLDER")

        dataFrame = tk.Frame(parent, width=430, bd=0, bg="white")
        dataFrame.columnconfigure(0, weight=1)
        dataFrame.columnconfigure(1, weight=1)
        dataFrame.rowconfigure(0, weight=1)
        dataFrame.rowconfigure(1, weight=1)
        dataFrame.rowconfigure(2, weight=1)
        dataFrame.rowconfigure(3, weight=1)
        dataFrame.rowconfigure(4, weight=1)
        dataFrame.rowconfigure(5, weight=1)

        self.l[0] = tk.Label(dataFrame, text="ID:", anchor="w", font=self.table_ifont, width=cell_width, bd=1,
                             relief="solid", bg="white")
        self.l[0].grid(row=0, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[1] = tk.Label(dataFrame, text="AssignmentID:", anchor="w", font=self.table_ifont, width=cell_width, bd=1,
                             relief="solid", bg="white")
        self.l[1].grid(row=1, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[2] = tk.Label(dataFrame, text="SkinType:", anchor="w", font=self.table_ifont, width=cell_width, bd=1,
                             relief="solid", bg="white")
        self.l[2].grid(row=2, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[3] = tk.Label(dataFrame, text="Date:", anchor="w", font=self.table_ifont, width=cell_width, bd=1,
                             relief="solid", bg="white")
        self.l[3].grid(row=3, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)

        self.l[4] = tk.Label(dataFrame, text="Path:", anchor="w", font=self.table_ifont, width=cell_width, bd=1,
                             relief="solid", bg="white")
        self.l[4].grid(row=4, column=0, sticky="ew", ipady=py, ipadx=ipx, padx=px)


        if self.table_version == 1:
            cell_width = 12
            self.d[0] = tk.Label(dataFrame, text="", font=self.table_nfont, width=cell_width, bd=2)
            self.d[0].grid(row=0, column=1, sticky="ew", pady=py, padx=px)
            self.d[1] = tk.Label(dataFrame, text="", font=self.table_nfont, width=cell_width, bd=2)
            self.d[1].grid(row=1, column=1, sticky="ew", pady=py, padx=px)
            self.d[2] = tk.Label(dataFrame, text="", font=self.table_nfont, width=cell_width, bd=2)
            self.d[2].grid(row=2, column=1, sticky="ew", pady=py, padx=px)
            self.d[3] = tk.Label(dataFrame, text="", font=self.table_nfont, width=cell_width, bd=2)
            self.d[3].grid(row=3, column=1, sticky="ew", pady=py, padx=px)
        elif self.table_version == 2:
            cell_width = 8
            self.d[0] = tk.Entry(dataFrame, textvariable=txt, bd=2, font=self.table_nfont, width=cell_width * 2)
            self.d[0].grid(row=0, column=1, pady=py, padx=px, sticky="ew")
            self.d[1] = tk.Entry(dataFrame, textvariable=txt, bd=2, font=self.table_nfont, width=cell_width * 2)
            self.d[1].grid(row=1, column=1, pady=py, padx=px, sticky="ew")
            self.d[2] = tk.Entry(dataFrame, textvariable=txt, bd=2, font=self.table_nfont, width=cell_width * 2)
            self.d[2].grid(row=2, column=1, pady=py, padx=px, sticky="ew")
            self.d[3] = tk.Entry(dataFrame, textvariable=txt, bd=2, font=self.table_nfont, width=cell_width * 2)
            self.d[3].grid(row=3, column=1, pady=py, padx=px, sticky="ew")
            self.d[4] = tk.Entry(dataFrame, textvariable=txt, bd=2, font=self.table_nfont, width=cell_width * 2)
            self.d[4].grid(row=4, column=1, pady=py, padx=px, sticky="ew")

        self.changeData()  # Initialize data
        return dataFrame

    def createImageFrame(self, parent):
        imgFrame = tk.Frame(parent, bd=10, bg="white")
        imgFrame.columnconfigure(0, weight=1)
        imgFrame.columnconfigure(1, weight=3)
        imgFrame.columnconfigure(2, weight=1)
        imgFrame.rowconfigure(0, weight=1)

        self.display = tk.Canvas(imgFrame, bd=0, bg="#FFFFFF", highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, tags="IMG")
        self.display.grid(row=0, column=1, sticky="nsew", ipadx=10)
        return imgFrame

    def createBody(self):
        tempFrame = tk.Frame(self, bd=0, bg="white")
        tempFrame.pack(fill=tk.BOTH, expand=1)

        tempFrame.rowconfigure(0, weight=2)
        tempFrame.rowconfigure(1, weight=1)
        imageFrame = self.createImageFrame(tempFrame)
        tempFrame.columnconfigure(0, weight=1)
        imageFrame.grid(row=0, column=0, sticky="nsew")

        tempFrame.columnconfigure(1, weight=2)
        dataTable = self.createDataTable(tempFrame)
        dataTable.grid(row=0, column=1, sticky=tk.NSEW)
        return tempFrame

    def setTheme(self):
        self.table_ifont = tkfont.Font(family='Helvetica', size=20, slant="roman")
        self.table_nfont = tkfont.Font(family='Helvetica', size=20)
        self.generatorTitleImage = ImageTk.PhotoImage(Image.open("Images/GeneratorPage/generatorTitleImage.png"))
        self.tgti = Image.open("Images/GeneratorPage/generatorTitleImage.png")
        self.placeholderImage = Image.open("Files/Faces/Face_2020-02-27_02-52-56.png")
        self.returnButtonImage = ImageTk.PhotoImage(Image.open("Images/returnButton.png"))
        self.randomButtonImage = ImageTk.PhotoImage(Image.open("Images/GeneratorPage/randomButton.png"))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white", width=1200, height=650)
        self.controller = controller
        self.dataSet = controller.database.get_data_from_table("Appearance")
        self.setTheme()  # inicjalizacja img, font

        self.d = [tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""),tk.Label(self, text="")]
        self.l = [tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""), tk.Label(self, text=""),tk.Label(self, text="")]

        self.x = self.winfo_reqwidth()
        self.y = self.winfo_reqheight()

        self.image = ImageTk.PhotoImage(self.placeholderImage)
        # self.bind("<Configure>", self.resize)

        self.createHeader().pack(side=tk.TOP, expand=False)  # Create header
        self.createBody().pack(expand=True, pady=10)  # Create body

        return_button = tk.Button(self, text="Return", image=self.returnButtonImage, bd=0, bg="white",
                                  command=lambda: controller.show_frame("Menu"))  # Create return button
        return_button.pack(side=tk.LEFT, padx=10, pady=5)

        random_button = tk.Button(self, text="Random", image=self.randomButtonImage, bd=0, bg="white",
                                  command=lambda: self.runGenerator())  # Create random button
        random_button.pack(side=tk.RIGHT, fill=tk.X, padx=10, pady=5)
