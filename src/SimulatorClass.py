import tkinter as tk
import tkinter.font as tkFont

class VisualCircuitSimulator:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.NazovTeorie = {"Vypínač","ASdsadsadsadsadsad"}

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        baseFontSize = int(min(screenWidth, screenHeight) * 0.02)
        self.fontSize = tkFont.Font(family="Arial", size=baseFontSize)
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)
#-------------------------------------------------------------------------------------
        panelFrame = tk.Frame(self.root, relief="groove", bd=5, bg="blue")
        panelFrame.place(x=0, rely=0.1, relwidth=0.2, relheight=0.9)  

        scrollCanvas = tk.Canvas(panelFrame, bg="blue")
        scrollCanvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(panelFrame, orient="vertical", command=scrollCanvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.buttonContainer = tk.Frame(scrollCanvas, bg="blue")
        scrollCanvas.create_window((0, 0), window=self.buttonContainer, anchor="nw")

        scrollCanvas.configure(yscrollcommand=scrollbar.set)
        self.buttonContainer.bind("<Configure>", lambda event: scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all")))
#-------------------------------------------------------------------------------------
        for circuitName in self.NazovTeorie:
            button = tk.Button(
                self.buttonContainer,
                width=int(self.Cw*1.2),
                text=f"{circuitName}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda: self.buttonAction(circuitName)
            )
            button.pack(pady=5, padx=3, anchor="w")  
#-------------------------------------------------------------------------------------
    def buttonAction(self, circuit):
        self.ClearFunction()
        self.canvas = tk.Canvas(self.root, bg="white", relief="ridge",bd=5)
        self.canvas.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.5)
        self.OpenList.append(self.canvas)
        print(circuit)
        
        
        self.drawCircuit1()
#-------------------------------------------------------------------------------------
    def drawCircuit1(self):
        switchState = {"is_on": False}  
        # How big the circuit is
        scale = int(self.Cw*0.15)
        # Battery
        self.canvas.create_line(50 * scale, 100 * scale, 50 * scale, 150 * scale, width=3)  # Battery wire
        self.canvas.create_line(35 * scale, 100 * scale, 65 * scale, 100 * scale, width=3)  # +
        self.canvas.create_line(40 * scale, 105 * scale, 60 * scale, 105 * scale, width=3)  # -
        positiveLabel = tk.Label(self.canvas, text="+", font=self.fontSize, bg="white", fg="red")
        positiveLabel.place(relx=0.05, rely=0.25)
        negativeLabel = tk.Label(self.canvas, text="_", font=self.fontSize, bg="white", fg="black")
        negativeLabel.place(relx=0.05, rely=0.4)
        # Wire from battery to switch
        self.canvas.create_line(50 * scale, 150 * scale, 150 * scale, 150 * scale, width=3)
        # Switch
        switchLine = self.canvas.create_line(150 * scale, 150 * scale, 250 * scale, 120 * scale, width=3, fill="white")
        # Wire to lamp
        self.canvas.create_line(250 * scale, 150 * scale, 350 * scale, 150 * scale, width=3)
        self.canvas.itemconfig(switchLine, fill="black")
        # Lamp 
        self.bulb = self.canvas.create_oval(350 * scale, 130 * scale, 380 * scale, 160 * scale, fill="white", outline="black")
        self.canvas.create_text(365 * scale, 170 * scale, text="Žiarovka", anchor="center", font=("Arial", 10 * scale))
        # Return path
        self.canvas.create_line(380 * scale, 150 * scale, 450 * scale, 150 * scale, width=3)  # Wire after bulb
        self.canvas.create_line(450 * scale, 150 * scale, 450 * scale, 50 * scale, width=3)  # Upward wire
        self.canvas.create_line(450 * scale, 50 * scale, 50 * scale, 50 * scale, width=3)  # Top wire
        self.canvas.create_line(50 * scale, 50 * scale, 50 * scale, 150 * scale, width=3)  # Back to battery
        
        def toggleSwitch():
            switchState["is_on"] = not switchState["is_on"]  
            
            if switchState["is_on"]:
                
                self.canvas.coords(switchLine, 150 * scale, 150 * scale, 250 * scale, 150 * scale)
                self.canvas.itemconfig(self.bulb, fill="yellow")  
            else:
                
                self.canvas.coords(switchLine, 150 * scale, 150 * scale, 250 * scale, 120 * scale)
                self.canvas.itemconfig(self.bulb, fill="white")  

        # Switch button
        switchButton = tk.Button(self.canvas, text="Stlačiť",font=("Arial, 25") ,bg="white", fg="green",relief="solid",command=toggleSwitch)
        switchButton.place(relx=0.2, rely=0.7, relwidth=0.3,relheight=0.2)
#-------------------------------------------------------------------------------------