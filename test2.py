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


class Teoria:
    def __init__(self, root):
        self.root = root
        self.NazovTeorie = {"Ohm","Kapacita","Kirc","background"}

       
        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,y=Ch*10)  

       
        self.canvas = tk.Canvas(frame, width=Cw*20, height=Ch*80, bg="lime")
        self.canvas.pack(side="left", fill="both", expand=True)

        
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

       
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        
        self.button_frame = tk.Frame(self.canvas)

        
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

       
        for i in self.NazovTeorie:
            button = tk.Button(self.button_frame, text=f"{i}", relief="groove",bd=1, bg="black",fg="white", width=int(Cw*1.82),height=int(Ch*0.2)
                               ,font=("Arial, 15") ,command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  # Add some vertical space between buttons

        # Update scrollregion to encompass the button frame
        self.button_frame.update_idletasks()  # Update frame to get the correct size
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Set scroll region
        
    def button_action(self, button_number):
        
       
        filename = f"{button_number}.jpg"
       
        image_path = os.path.join("Teoria", f"{filename}")
    
        pil_image = Image.open(image_path)
        imageT = ImageTk.PhotoImage(pil_image)

        #try:
           # with open(filepath, 'r') as file:
           #     content = file.read()
        Current = tk.Label(root,image=imageT)
        Current.place(x=Cw*25,y=Ch*10)
        
        #place(x=Cw*50,y=100)
           
        #except FileNotFoundError:
         #   messagebox.showerror("Error", f"File {filename} not found in {text_folder}!")
class Calculator:
    def __init__(self, root):
        self.root = root
        self.NazovOperacie = {"Ohmov zákon"}

        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,y=Ch*10)  
 
        self.canvas = tk.Canvas(frame, width=Cw*20, height=Ch*80, bg="lime")
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
        
    def button_action(self, button_number):
        
       
        filename = f"{button_number}.jpg"
       
        image_path = os.path.join("Teoria", f"{filename}")
    
        pil_image = Image.open(image_path)
        imageT = ImageTk.PhotoImage(pil_image)

        
        Current = tk.Label(root,image=imageT)
        Current.place(x=Cw*25,y=Ch*10)
        

def RunTeoriaTab():
    Teoria(root)   
    
def RunCalculator():
    Calculator(root) 

        
TeoriaOpenButton= tk.Button(root,text="Teória",width=int(Cw*2),height=int(Ch*0.29),command=RunTeoriaTab)
TeoriaOpenButton.place(x=Cw*20,y=Ch*1.3)
CalculatorOpenButton = tk.Button(root,text="Kalkulačka",font=("Arial, 15"),bg="gold",bd=None,width=int(Cw*2),height=int(Ch*0.29),command=RunCalculator)
CalculatorOpenButton.place(x=Cw*40,y=Ch*1.3)

ClassTeory = RunTeoriaTab()


root.mainloop()