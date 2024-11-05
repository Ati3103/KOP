import tkinter as tk
import tkinter.font as tkFont
from TeoriaClass import Teoria
from CalculatorClass import Calculator

#---------------------------------------------------
root = tk.Tk()
root.attributes("-fullscreen", True)
image = tk.PhotoImage(file="background.png")
#---------------------------------------------------
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
baseFontSize = int(min(screenWidth, screenHeight) * 0.03)
fontSize = tkFont.Font(family="Arial", size=baseFontSize)
#----------------------------------------------------------------------------------------------
bgLabel = tk.Label(root, width=screenWidth, height=screenHeight, image=image)
bgLabel.pack()
#----------------------------------------------------------------------------------------------------------------------------------------  
headerLabel = tk.Label(root, width=screenWidth,bd=5, relief="solid", bg="gold")
headerLabel.place(x=0, y=0,relheight=0.068)
#----------------------------------------------------------------------------------------------------------------------------------------
closeButton = tk.Button(root, text="X", font=fontSize, fg="white", bg="red",bd=5, relief="solid",  command=root.destroy)
closeButton.place(relx=1.0, rely=0.001,relwidth=0.05,relheight=0.065 ,anchor="ne")
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
TeoriaOpenButton= tk.Button(root,text="Teória",font=fontSize,bg="lightblue",bd=None,command=RunTeoriaTab)
TeoriaOpenButton.place(relx=0.3, rely=0.005, relwidth=0.08,relheight=0.06)
CalculatorOpenButton = tk.Button(root,text="Kalkulačka",font=fontSize,bg="lightblue",bd=None,command=RunCalculator)
CalculatorOpenButton.place(relx=0.4, rely=0.005, relwidth=0.13,relheight=0.06)
ClassTeory = RunTeoriaTab()
root.mainloop()
#-------------------------------------------------------------------------------------

#TeoriaOpenButton= tk.Button(root,text="Teória",font=(f"Arial, {int(Cw*0.9)}"),bg="lightblue",bd=None,width=int(Cw*1),height=int(Ch*0.25),command=RunTeoriaTab)
#TeoriaOpenButton.place(x=Cw*30,y=Ch*0.7)