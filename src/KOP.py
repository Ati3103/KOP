import tkinter as tk
from tkinter import messagebox
from TeoriaClass import Teoria
from CalculatorClass import Calculator

#---------------------------------------------------
root = tk.Tk()
root.attributes("-fullscreen", True)
image = tk.PhotoImage(file="background.png")
#---------------------------------------------------
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
#---------------------------------------------------
Cw = int(screenWidth/100)
Ch = int(screenHeight/100)
#----------------------------------------------------------------------------------------------
bgLabel = tk.Label(root, width=screenWidth, height=screenHeight, image=image)
bgLabel.pack()
#----------------------------------------------------------------------------------------------------------------------------------------  
headerLabel = tk.Label(root, width=screenWidth, height=int(Ch * 0.4),bd=5, relief="solid", bg="gold")
headerLabel.place(x=0, y=0)
#----------------------------------------------------------------------------------------------------------------------------------------
closeButton = tk.Button(root, text="X", font=("Arial", 24), fg="white", bg="red",bd=5, relief="solid", width=4, command=root.destroy)
closeButton.place(relx=1.0, rely=0.001, anchor="ne")
#----------------------------------------------------------------------------------------------------------------------------------------
open_tabs = []
#-------------------------------
def ClearTabs():
    for widget in open_tabs:
        widget.destroy()
#-------------------------------------------------------------------------------------
def RunTeoriaTab():
    ClearTabs()
    Teoria(root, ClearTabs, open_tabs)   
#-------------------------------------------------------------------------------------    
def RunCalculator():
    ClearTabs()
    Calculator(root, ClearTabs, open_tabs) 
#-------------------------------------------------------------------------------------
TeoriaOpenButton= tk.Button(root,text="Teória",font=(f"Arial, {int(Cw*0.9)}"),bg="lightblue",bd=None,width=int(Cw*1),height=int(Ch*0.25),command=RunTeoriaTab)
TeoriaOpenButton.place(x=Cw*30,y=Ch*0.7)
CalculatorOpenButton = tk.Button(root,text="Kalkulačka",font=(f"Arial, {int(Cw*0.9)}"),bg="lightblue",bd=None,width=int(Cw*1),height=int(Ch*0.25),command=RunCalculator)
CalculatorOpenButton.place(x=Cw*45,y=Ch*0.7)
ClassTeory = RunTeoriaTab()
root.mainloop()
#-------------------------------------------------------------------------------------