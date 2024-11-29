import tkinter as tk
import tkinter.font as tkFont

class VisualCircuitSimulator:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.CircuitName = ["Klasický vypínač","Schodišťový vypínač"]

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
        for circuitName in self.CircuitName:
            button = tk.Button(
                self.buttonContainer,
                width=int(self.Cw * 1.2),
                text=f"{circuitName}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda circuitName=circuitName: self.buttonAction(circuitName)  
            )
            button.pack(pady=5, padx=3, anchor="w")
#-------------------------------------------------------------------------------------
    def buttonAction(self, circuit):
        self.ClearFunction()
        self.canvas = tk.Canvas(self.root, bg="white", relief="ridge",bd=5)
        self.canvas.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.5)
        self.OpenList.append(self.canvas)
        print(circuit)
        
        if circuit == "Klasický vypínač":
            self.drawCircuit1() 
        elif circuit == "Schodišťový vypínač":
            self.drawCircuit2()    
           
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
        switch = self.canvas.create_line(150 * scale, 150 * scale, 180 * scale, 120 * scale, width=3, fill="white")
        # Wire to lamp
        self.canvas.create_line(190 * scale, 150 * scale, 350 * scale, 150 * scale, width=3)
        self.canvas.itemconfig(switch, fill="red")
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
                
                self.canvas.coords(switch, 150 * scale, 150 * scale, 190 * scale, 150 * scale)
                self.canvas.itemconfig(self.bulb, fill="yellow")
                self.canvas.itemconfig(switch, fill="green")  
            else:
                
                self.canvas.coords(switch, 150 * scale, 150 * scale, 180 * scale, 120 * scale)
                self.canvas.itemconfig(self.bulb, fill="white")
                self.canvas.itemconfig(switch, fill="red")  

        # Switch button
        switchButton = tk.Button(self.canvas, text="Vypínač",font=("Arial, 25") ,bg="white", fg="green",relief="solid",command=toggleSwitch)
        switchButton.place(relx=0.2, rely=0.7, relwidth=0.3,relheight=0.2)
    
    def drawCircuit2(self):
        switchState1 = {"is_on": True}
        switchState2 = {"is_on": False} 
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
        self.canvas.create_line(50 * scale, 150 * scale, 80 * scale, 150 * scale, width=3)
        # Switches
        switch1 = self.canvas.create_line(80 * scale, 150 * scale, 110 * scale, 120 * scale, width=3, fill="red")
        switch2 = self.canvas.create_line(220 * scale, 180 * scale, 250 * scale, 150 * scale, width=3, fill="red")
        #Lines between switches
        self.upperLine = self.canvas.create_line(110 * scale, 120 * scale, 220 * scale, 120 * scale, width=3, fill="black")
        self.lowerLine = self.canvas.create_line(110 * scale, 180 * scale, 220 * scale, 180 * scale, width=3, fill="black")
        # Wire to lamp
        self.canvas.create_line(250 * scale, 150 * scale, 350 * scale, 150 * scale, width=3)
        self.canvas.itemconfig(switch1, fill="red")
        self.canvas.itemconfig(switch2, fill="red")
        # Lamp 
        self.bulb = self.canvas.create_oval(350 * scale, 130 * scale, 380 * scale, 160 * scale, fill="white", outline="black")
        self.canvas.create_text(365 * scale, 170 * scale, text="Žiarovka", anchor="center", font=("Arial", 10 * scale))
        # Return path
        self.canvas.create_line(380 * scale, 150 * scale, 450 * scale, 150 * scale, width=3)  # Wire after bulb
        self.canvas.create_line(450 * scale, 150 * scale, 450 * scale, 50 * scale, width=3)  # Upward wire
        self.canvas.create_line(450 * scale, 50 * scale, 50 * scale, 50 * scale, width=3)  # Top wire
        self.canvas.create_line(50 * scale, 50 * scale, 50 * scale, 150 * scale, width=3)  # Back to battery
        
        #Switch logic
        def detectSwitchStates():
            print(switchState1, switchState2)
            if switchState1  ["is_on"] and switchState2  ["is_on"]:
                self.canvas.itemconfig(self.bulb, fill="yellow")
                self.canvas.itemconfig(switch1, fill="green")
                self.canvas.itemconfig(switch2, fill="green")
                
            elif not switchState1 ["is_on"] and not switchState2 ["is_on"]:
                self.canvas.itemconfig(self.bulb, fill="yellow")
                self.canvas.itemconfig(switch1, fill="green")
                self.canvas.itemconfig(switch2, fill="green")
                
            elif switchState1 ["is_on"] and not switchState2 ["is_on"]:
                self.canvas.itemconfig(self.bulb, fill="white")
                self.canvas.itemconfig(switch1, fill="red")
                self.canvas.itemconfig(switch2, fill="red")   
                  
            elif not switchState1 ["is_on"] and switchState2 ["is_on"]:
                
                self.canvas.itemconfig(self.bulb, fill="white") 
                self.canvas.itemconfig(switch1, fill="red")
                self.canvas.itemconfig(switch2, fill="red")        
        
        #Changing switch positions after activation
        def toggleSwitch1():
            switchState1["is_on"] = not switchState1["is_on"]  

            if switchState1["is_on"]:    
                self.canvas.coords(switch1, 80 * scale, 150 * scale, 110 * scale, 120 * scale)     
            else: 
                self.canvas.coords(switch1, 80 * scale, 150 * scale, 110 * scale, 180 * scale)      
            detectSwitchStates()     
        def toggleSwitch2():
            switchState2["is_on"] = not switchState2["is_on"]   
            if switchState2["is_on"]:    
                self.canvas.coords(switch2, 220 * scale, 120 * scale, 250 * scale, 150 * scale)
            else:   
                self.canvas.coords(switch2, 220 * scale, 180 * scale, 250 * scale, 150 * scale)  
            detectSwitchStates() 

        # Buttons for switches
        switchButton1 = tk.Button(self.canvas, text="Vypínač 1",font=self.fontSize ,bg="white", fg="green",relief="solid",command=toggleSwitch1)
        switchButton1.place(relx=0.05, rely=0.7, relwidth=0.2,relheight=0.1)
        switchButton2 = tk.Button(self.canvas, text="Vypínač 2",font=self.fontSize ,bg="white", fg="green",relief="solid",command=toggleSwitch2)
        switchButton2.place(relx=0.3, rely=0.7, relwidth=0.2,relheight=0.1)
#-------------------------------------------------------------------------------------