import tkinter as tk
import tkinter.font as tkFont
from TeoriaClass import Teoria
from CalculatorClass import Calculator
from SimulatorClass import VisualCircuitSimulator
from QuizClass import Quiz
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
headerLabel = tk.Label(root, width=screenWidth,bd=5, relief="solid", bg="lightblue")
headerLabel.place(x=0, y=0,relheight=0.068)
#----------------------------------------------------------------------------------------------------------------------------------------
closeButton = tk.Button(root, text="X", font=fontSize, fg="white", bg="red",bd=5, relief="solid",  command=root.destroy)
closeButton.place(relx=1.0, rely=0.001,relwidth=0.05,relheight=0.065 ,anchor="ne")
#----------------------------------------------------------------------------------------------------------------------------------------
openTabs = []
openButtons = []
#-------------------------------
def ClearTabs():
    for widget in openTabs:
        widget.destroy()
#-------------------------------------------------------------------------------------
def RemoveButtons():
    for button in openButtons:
        button.place_forget()
def RunTeoriaTab():
    ClearTabs()
    RemoveButtons()
    Teoria(root, ClearTabs,RemoveButtons, openTabs,openButtons,0)   
#-------------------------------------------------------------------------------------    
def RunCalculator():
    ClearTabs()
    RemoveButtons()
    Calculator(root, ClearTabs, openTabs) 
#-------------------------------------------------------------------------------------  
def RunSimulation():
    ClearTabs()
    RemoveButtons()
    VisualCircuitSimulator(root, ClearTabs, openTabs) 
#-------------------------------------------------------------------------------------
def RunQuiz():
    ClearTabs()
    RemoveButtons()
    Quiz() 
#-------------------------------------------------------------------------------------
TeoriaOpenButton= tk.Button(root,text="Teória",font=fontSize,bg="lightblue",bd=None,command=RunTeoriaTab)
TeoriaOpenButton.place(relx=0.001, rely=0.005, relwidth=0.1,relheight=0.06)
CalculatorOpenButton = tk.Button(root,text="Kalkulačka",font=fontSize,bg="lightblue",bd=None,command=RunCalculator)
CalculatorOpenButton.place(relx=0.101, rely=0.005, relwidth=0.18,relheight=0.06)
SimulatorOpenButton = tk.Button(root,text="Simulácie obvodov",font=fontSize,bg="lightblue",bd=None,command=RunSimulation)
SimulatorOpenButton.place(relx=0.281, rely=0.005, relwidth=0.27,relheight=0.06)
QuizOpenButton = tk.Button(root,text="Kvíz z teórie",font=fontSize,bg="lightblue",bd=None,command=RunQuiz)
QuizOpenButton.place(relx=0.551, rely=0.005, relwidth=0.27,relheight=0.06)
ClassTeory = RunTeoriaTab()
root.mainloop()
#-------------------------------------------------------------------------------------

