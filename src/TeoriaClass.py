import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import os

class Teoria:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.NazovTeorie = {"Ohm","Kapacita","Napätie"}

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        baseFontSize = int(min(screenWidth, screenHeight) * 0.03)
        self.fontSize = tkFont.Font(family="Arial", size=baseFontSize)
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)
       
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
                               font=self.fontSize ,width=int(self.Cw*0.9),height=int(self.Ch*0.1),command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  
#-------------------------------------------------------------------------------------
        self.button_frame.update_idletasks()  # Update frame to get the correct size
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Set scroll region
#-------------------------------------------------------------------------------------
    def button_action(self, button_name):
        self.ClearFunction()
        image_path = os.path.join("Teoria", f"{button_name}.png")

        if os.path.exists(image_path):
           
            img = tk.PhotoImage(file=image_path)
         
            img_label = tk.Label(self.root, image=img,relief="solid")
            img_label.image = img  
            img_label.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.7)  
            self.OpenList.append(img_label)
        else:
            messagebox.showerror("Chyba", f"Materiál '{image_path}' sa nenašiel.")
#-------------------------------------------------------------------------------------        