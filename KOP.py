import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox


#---------------------------------------------------
root = tk.Tk()
root.attributes("-fullscreen", True)
image = tk.PhotoImage(file="background.png")
#---------------------------------------------------
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#Calculation_of_screen_resolution
Cw = int(screen_width/100)
Ch = int(screen_height/100)
#----------------------------------------------------------------------------------------------
bg_label = tk.Label(root, width=screen_width, height=screen_height, image=image)
bg_label.pack()
#----------------------------------------------------------------------------------------------------------------------------------------  
header_label = tk.Label(root, width=screen_width, height=int(Ch * 0.4),bd=5, relief="solid", bg="gold")
header_label.place(x=0, y=0)
#----------------------------------------------------------------------------------------------------------------------------------------
close_button = tk.Button(root, text="X", font=("Arial", 24), fg="white", bg="red",bd=5, relief="solid", width=4, command=root.destroy)
close_button.place(relx=1.0, rely=0.001, anchor="ne")
#----------------------------------------------------------------------------------------------------------------------------------------
open_tabs = []

def ClearTabs():
    for widget in open_tabs:
        widget.destroy()


class Teoria:
    def __init__(self, root):
        self.root = root
        self.NazovTeorie = {"Ohm","Kapacita","Kirc"}

       
        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,y=Ch*10)  

       
        self.canvas = tk.Canvas(frame, width=Cw*20, height=Ch*80, bg="lightblue")
        self.canvas.pack(side="left", fill="both", expand=True)

        
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

       
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        
        self.button_frame = tk.Frame(self.canvas)

        
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

       
        for i in self.NazovTeorie:
            button = tk.Button(self.button_frame, text=f"{i}", relief="groove",bd=1, bg="black",fg="white", width=int(Cw*1.82),height=int(Ch*0.2)
                               ,font=("Arial, 15") ,command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  

        self.button_frame.update_idletasks()  # Update frame to get the correct size
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Set scroll region
        
    def button_action(self, button_name):
        ClearTabs()
        image_path = f"{button_name}.png"

        if os.path.exists(image_path):
           
            img = tk.PhotoImage(file=image_path)
         
            img_label = tk.Label(root, image=img,width=int(Cw*50),height=int(Ch*25),relief="solid")
            img_label.image = img  
            img_label.place(x=Cw * 25, y=Ch * 15)  
            open_tabs.append(img_label)
        else:
            messagebox.showerror("Chyba", f"Obrázok '{image_path}' sa nenašiel.")
        
class Calculator:
    def __init__(self, root):
        self.root = root
        self.NazovOperacie = {"Ohmov zákon","Výkon"}

        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,y=Ch*10)  
 
        self.canvas = tk.Canvas(frame, width=Cw*20, height=Ch*80, bg="lightblue")
        self.canvas.pack(side="left", fill="both", expand=True)
   
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
    
        self.button_frame = tk.Frame(self.canvas)
      
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

       
        for i in self.NazovOperacie:
            button = tk.Button(self.button_frame, text=f"{i}", relief="groove",bd=1, bg="black",fg="white", width=int(Cw*1.82),height=int(Ch*0.2)
                               ,font=("Arial, 15") ,command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  

       
        self.button_frame.update_idletasks()  
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  
        
    def button_action(self, button_name):
       if button_name == "Ohmov zákon":
            self.CalculateOhmsLaw() 
       elif button_name == "Výkon":
            self.CalculatePower()            
    
    def CalculateOhmsLaw(self):
        ClearTabs()
        self.result = 0
        frame = tk.Frame(self.root, width=int(Cw*70), height=int(Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(x=Cw*30, y=Ch*30)
        open_tabs.append(frame)
      
        self.entryR = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryR.place(x=95, y=10)
        self.entryU = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryU.place(x=95, y=50)
        self.entryI = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryI.place(x=95, y=90)
        
        self.labelR = tk.Label(frame,text="R [Ω]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelR.place(x=10, y=10)
        self.labelU = tk.Label(frame,text="U [V]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelU.place(x=10, y=50)
        self.labelI = tk.Label(frame,text="I  [A]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelI.place(x=17, y=90)

        
        self.Result = tk.Label(frame, text=f"Výsledok: {self.result} ",font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Result.place(x=470, y=70)

        self.Info = tk.Label(frame, text=f"Vzorce: R=U/I , U=I⋅R , I=U/R",font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Info.place(x=470, y=20)
        
        def Calculate():
            R = self.entryR.get()
            U = self.entryU.get()
            I = self.entryI.get()

            try:
                R = float(R) if R else None
                U = float(U) if U else None
                I = float(I) if I else None

                if R is None and U is not None and I is not None:
                    self.result = (f"{U / I} Ω")
                elif U is None and R is not None and I is not None:
                    self.result = (f"{R * I} V")
                elif I is None and R is not None and U is not None:
                    self.result = (f"{U / R} A")
                else:
                    self.result = "Chyba: Nevhodné hodnoty"
            except ValueError:
                self.result = "Chyba: Nevhodné hodnoty"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font="Arial, 15",bd=2, relief="solid", command=Calculate)
        self.StartButton.place(x=150, y=150)
   
    def CalculatePower(self):
        ClearTabs()
        self.result = 0
        frame = tk.Frame(self.root, width=int(Cw*70), height=int(Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(x=Cw*30, y=Ch*30)
        open_tabs.append(frame)
      
        self.entryR = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryR.place(x=95, y=10)
        self.entryU = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryU.place(x=95, y=50)
        self.entryI = tk.Entry(frame,font=("Arial, 25"),bg="DeepSkyBlue4")
        self.entryI.place(x=95, y=90)
        
        self.labelR = tk.Label(frame,text="R [Ω]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelR.place(x=10, y=10)
        self.labelU = tk.Label(frame,text="U [V]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelU.place(x=10, y=50)
        self.labelI = tk.Label(frame,text="I  [A]",font=("Arial, 25"),bg="DeepSkyBlue4",fg="white")
        self.labelI.place(x=17, y=90)

        
        self.Result = tk.Label(frame, text=f"Výsledok: P = {self.result} W",font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Result.place(x=470, y=70)

        self.Info = tk.Label(frame, text=f"Vzorce: P=U⋅I , P=I^2⋅R , P=U^2/R",font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Info.place(x=470, y=20)
        
        def Calculate():
            R = self.entryR.get()
            U = self.entryU.get()
            I = self.entryI.get()

            try:
                R = float(R) if R else None
                U = float(U) if U else None
                I = float(I) if I else None

                if U is not None and I is not None:
                    self.result = U * I
                elif I is not None and R is not None:
                    self.result = I**2 * R
                elif U is not None and R is not None:
                    self.result = (U**2) / R
                else:
                    self.result = "Chyba: Nevhodné hodnoty"
            except ValueError:
                self.result = "Chyba: Nevhodné hodnoty"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")

        # Button to trigger calculation
        self.StartButton = tk.Button(frame, text="Vypočítať",font="Arial, 15",bd=2, relief="solid", command=Calculate)
        self.StartButton.place(x=150, y=150)
    
def RunTeoriaTab():
    Teoria(root)   
    
def RunCalculator():
    Calculator(root) 

        
TeoriaOpenButton= tk.Button(root,text="Teória",font=("Arial, 14"),bg="lightblue",bd=None,width=int(Cw*1),height=int(Ch*0.25),command=RunTeoriaTab)
TeoriaOpenButton.place(x=Cw*30,y=Ch*0.7)
CalculatorOpenButton = tk.Button(root,text="Kalkulačka",font=("Arial, 14"),bg="lightblue",bd=None,width=int(Cw*1),height=int(Ch*0.25),command=RunCalculator)
CalculatorOpenButton.place(x=Cw*45,y=Ch*0.7)

ClassTeory = RunTeoriaTab()


root.mainloop()