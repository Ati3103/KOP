import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Teoria:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.NazovTeorie = {"Ohm","Kapacita","Napätie","Prúd","Kirchhoffove Zákony"}
        

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        baseFontSize = int(min(screenWidth, screenHeight) * 0.02)
        self.fontSize = tkFont.Font(family="Arial", size=baseFontSize)
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)
        self.ImageW = int(screenWidth * 0.7)  
        self.ImageH = int(screenHeight * 0.8)
       
        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,rely=0.1)  
#-------------------------------------------------------------------------------------
        self.canvas = tk.Canvas(frame, width=self.Cw*20, height=self.Ch*80, bg="lightblue")
        self.canvas.pack(side="left", fill="both", expand=True)
#-------------------------------------------------------------------------------------
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
#-------------------------------------------------------------------------------------
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.button_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")
#-------------------------------------------------------------------------------------
        for i in self.NazovTeorie:
            button = tk.Button(self.button_frame, text=f"{i}", relief="groove",bd=1, bg="black",fg="white", 
                               font=self.fontSize ,width=int(self.Cw*1),height=int(self.Ch*0.1),command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  
#-------------------------------------------------------------------------------------
        self.button_frame.update_idletasks()  
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  
#-------------------------------------------------------------------------------------
    def button_action(self, button_name):
        self.ClearFunction()
        imagePath = Image.open(f"Teoria/{button_name}.png")
        resizedImage = imagePath.resize((self.ImageW, self.ImageH))
        tkImage = ImageTk.PhotoImage(resizedImage)
        imgLabel = tk.Label(self.root, image=tkImage,relief="solid")
        imgLabel.image = tkImage  
        imgLabel.place(relx=0.23,rely=0.1)  
        self.OpenList.append(imgLabel)
       
#-------------------------------------------------------------------------------------        