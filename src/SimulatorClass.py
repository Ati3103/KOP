import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VisualCircuitSimulator:
    def __init__(self, root, clearFunction, openTabs):        
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.CircuitName = ["Klasický vypínač","Schodišťový vypínač","Prúd","RLC grafy","Transformátor", "Napäťový delič"]
        
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        baseFontSize = int(min(screenWidth, screenHeight) * 0.02)
        self.fontSize = tkFont.Font(family="Arial", size=baseFontSize)
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)
#-------------------------------------------------------------------------------------
      
        panelFrame = tk.Frame(self.root, relief="groove", bd=5, bg="blue")
        panelFrame.place(x=0, rely=0.1, relwidth=0.2, relheight=0.9)  
#--------
       
        scrollCanvas = tk.Canvas(panelFrame, bg="blue", highlightthickness=0)
        scrollCanvas.pack(side="left", fill="both", expand=True)

      
        scrollbar = tk.Scrollbar(panelFrame, orient="vertical", command=scrollCanvas.yview)
        scrollbar.pack(side="right", fill="y")

       
        self.buttonContainer = tk.Frame(scrollCanvas, bg="blue")
        scrollCanvas.create_window((0, 0), window=self.buttonContainer, anchor="nw")

       
        scrollCanvas.configure(yscrollcommand=scrollbar.set)

        
        def update_scrollregion(event):
            scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all"))

        self.buttonContainer.bind("<Configure>", update_scrollregion)

       
        def on_mousewheel(event):
            scrollCanvas.yview_scroll(-1 * int(event.delta / 120), "units")

        scrollCanvas.bind_all("<MouseWheel>", on_mousewheel)
        
#-------------------------------------------------------------------------------------
        for circuitName in self.CircuitName:
            button = tk.Button(
                self.buttonContainer,
                text=f"{circuitName}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda circuitName=circuitName: self.buttonAction(circuitName)  
            )
            button.pack(pady=5, padx=3, anchor="w", fill="x")
#-------------------------------------------------------------------------------------   
    def buttonAction(self, circuit):
        self.ClearFunction()
        self.canvas = tk.Canvas(self.root, bg="white", relief="ridge",bd=5)
        self.canvas.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)
        self.OpenList.append(self.canvas)
        
        
        if circuit == "Klasický vypínač" :
            self.drawCircuit1()     
        elif circuit == "Schodišťový vypínač":
            self.drawCircuit2()  
        elif circuit == "Prúd":
            self.drawCircuit3() 
        elif circuit == "RLC grafy":
            self.drawCircuit4() 
        elif circuit == "Transformátor":
            self.drawCircuit5() 
        elif circuit == "Napäťový delič":
            self.drawCircuit6()        
           
#-------------------------------------------------------------------------------------
    def drawCircuit1(self):
        switchState = {"is_on": False}  
       
        scale = int(self.Cw*0.17)
       
        self.canvas.create_line(50 * scale, 100 * scale, 50 * scale, 150 * scale, width=3)  
        self.canvas.create_line(35 * scale, 100 * scale, 65 * scale, 100 * scale, width=3)  
        self.canvas.create_line(40 * scale, 105 * scale, 60 * scale, 105 * scale, width=3)  
        positiveLabel = tk.Label(self.canvas, text="+", font=self.fontSize, bg="white", fg="red")
        positiveLabel.place(relx=0.05, rely=0.25)
        negativeLabel = tk.Label(self.canvas, text="_", font=self.fontSize, bg="white", fg="black")
        negativeLabel.place(relx=0.05, rely=0.4)
  
        self.canvas.create_line(50 * scale, 150 * scale, 150 * scale, 150 * scale, width=3)
       
        switch = self.canvas.create_line(150 * scale, 150 * scale, 180 * scale, 120 * scale, width=3, fill="white")
       
        self.canvas.create_line(190 * scale, 150 * scale, 350 * scale, 150 * scale, width=3)
        self.canvas.itemconfig(switch, fill="red")
      
        self.bulb = self.canvas.create_oval(350 * scale, 130 * scale, 380 * scale, 160 * scale, fill="white", outline="black")
        self.canvas.create_text(365 * scale, 170 * scale, text="Žiarovka", anchor="center", font=("Arial", 10 * scale))
       
        self.canvas.create_line(380 * scale, 150 * scale, 450 * scale, 150 * scale, width=3)  
        self.canvas.create_line(450 * scale, 150 * scale, 450 * scale, 50 * scale, width=3)  
        self.canvas.create_line(450 * scale, 50 * scale, 50 * scale, 50 * scale, width=3)  
        self.canvas.create_line(50 * scale, 50 * scale, 50 * scale, 150 * scale, width=3)  
        
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

       
        switchButton = tk.Button(self.canvas, text="Vypínač",font=("Arial, 25") ,bg="white", fg="green",relief="solid",command=toggleSwitch)
        switchButton.place(relx=0.2, rely=0.7, relwidth=0.3,relheight=0.2)
#----------------------------------------------------------------------------------------------------------------------------------------------    
    def drawCircuit2(self):
        switchState1 = {"is_on": True}
        switchState2 = {"is_on": False} 
        
        scale = int(self.Cw*0.17)
        
        self.canvas.create_line(50 * scale, 100 * scale, 50 * scale, 150 * scale, width=3)  # Battery wire
        self.canvas.create_line(35 * scale, 100 * scale, 65 * scale, 100 * scale, width=3)  # +
        self.canvas.create_line(40 * scale, 105 * scale, 60 * scale, 105 * scale, width=3)  # -
        positiveLabel = tk.Label(self.canvas, text="+", font=self.fontSize, bg="white", fg="red")
        positiveLabel.place(relx=0.05, rely=0.25)
        negativeLabel = tk.Label(self.canvas, text="_", font=self.fontSize, bg="white", fg="black")
        negativeLabel.place(relx=0.05, rely=0.4)
       
        self.canvas.create_line(50 * scale, 150 * scale, 80 * scale, 150 * scale, width=3)
        
        switch1 = self.canvas.create_line(80 * scale, 150 * scale, 110 * scale, 120 * scale, width=3, fill="red")
        switch2 = self.canvas.create_line(220 * scale, 180 * scale, 250 * scale, 150 * scale, width=3, fill="red")
       
        self.upperLine = self.canvas.create_line(110 * scale, 120 * scale, 220 * scale, 120 * scale, width=3, fill="black")
        self.lowerLine = self.canvas.create_line(110 * scale, 180 * scale, 220 * scale, 180 * scale, width=3, fill="black")
       
        self.canvas.create_line(250 * scale, 150 * scale, 350 * scale, 150 * scale, width=3)
        self.canvas.itemconfig(switch1, fill="red")
        self.canvas.itemconfig(switch2, fill="red")
        
        self.bulb = self.canvas.create_oval(350 * scale, 130 * scale, 380 * scale, 160 * scale, fill="white", outline="black")
        self.canvas.create_text(365 * scale, 170 * scale, text="Žiarovka", anchor="center", font=("Arial", 10 * scale))
        
        self.canvas.create_line(380 * scale, 150 * scale, 450 * scale, 150 * scale, width=3)  # Wire after bulb
        self.canvas.create_line(450 * scale, 150 * scale, 450 * scale, 50 * scale, width=3)  # Upward wire
        self.canvas.create_line(450 * scale, 50 * scale, 50 * scale, 50 * scale, width=3)  # Top wire
        self.canvas.create_line(50 * scale, 50 * scale, 50 * scale, 150 * scale, width=3)  # Back to battery
        
        
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

        
        switchButton1 = tk.Button(self.canvas, text="Vypínač 1",font=self.fontSize ,bg="white", fg="green",relief="solid",command=toggleSwitch1)
        switchButton1.place(relx=0.05, rely=0.7, relwidth=0.2,relheight=0.1)
        switchButton2 = tk.Button(self.canvas, text="Vypínač 2",font=self.fontSize ,bg="white", fg="green",relief="solid",command=toggleSwitch2)
        switchButton2.place(relx=0.3, rely=0.7, relwidth=0.2,relheight=0.1)
#-------------------------------------------------------------------------------------
    def drawCircuit3(self):
        

        

        scale = int(self.Cw*0.12)
        voltage = 12  
        resistance1 = 10  
        resistance2 = 20  
        currentTotal = 0

        def calculateCurrents():
            nonlocal currentTotal
           
            current1 = voltage / resistance1
            current2 = voltage / resistance2
            currentTotal = current1 + current2

            currentLabel.config(text=f"Prúd celkovo: {currentTotal:.2f} A")
            voltageLabel.config(text=f"Napätie: {voltage:.2f} V")

           
            self.canvas.itemconfig(current1Text, text=f"I1 = {current1:.2f} A")
            self.canvas.itemconfig(current2Text, text=f"I2 = {current2:.2f} A")
            self.canvas.itemconfig(resistanceText1, text=f"R1 = {resistance1:.2f} Ω")
            self.canvas.itemconfig(resistanceText2, text=f"R2 = {resistance2:.2f} Ω")
            

        def updateCircuit(event=None):
            nonlocal voltage, resistance1, resistance2
            
            voltage = float(self.canvas.winfo_children()[4].get())
            resistance1 = float(self.canvas.winfo_children()[5].get())
            resistance2 = float(self.canvas.winfo_children()[6].get())
            calculateCurrents()

       
        self.canvas.create_line(50*scale, 160*scale, 50*scale, 300*scale, width=3)  # Vertikálny vodič zdroja
        self.canvas.create_line(30*scale, 250*scale, 70*scale, 250*scale, width=3)  # Horný vodič zdroja
        self.canvas.create_line(40*scale, 260*scale, 60*scale, 260*scale, width=3)  # Spodný vodič zdroja

        positiveLabel = tk.Label(self.canvas, text="+", font=self.fontSize, bg="white", fg="red")
        positiveLabel.place(relx=0.04, rely=0.47)

        negativeLabel = tk.Label(self.canvas, text="-", font=self.fontSize, bg="white", fg="black")
        negativeLabel.place(relx=0.041,rely=0.54)

       
        self.canvas.create_line(50*scale, 160*scale, 300*scale, 160*scale, width=3)  # Vodič k uzlu rezistorov
        resistor1 = self.canvas.create_rectangle(290*scale, 230*scale, 310*scale, 270*scale, outline="black", fill="white")
        resistor2 = self.canvas.create_rectangle(340*scale, 230*scale, 360*scale, 270*scale, outline="black", fill="white")
        
        self.canvas.create_line(200*scale, 160*scale, 350*scale, 160*scale, width=3)  # Vodič od prvého rezistora
        self.canvas.create_line(200*scale, 300*scale, 300*scale, 300*scale, width=3)  # Vodič od druhého rezistora
        
        self.canvas.create_line(300*scale, 160*scale, 300*scale, 230*scale, width=3)  # Vertikálny vodič medzi rezistormi
        self.canvas.create_line(300*scale, 270*scale, 300*scale, 300*scale, width=3)  # Vertikálny vodič medzi rezistormi
        self.canvas.create_line(350*scale, 160*scale, 350*scale, 230*scale, width=3)  # Vertikálny vodič medzi rezistormi
        self.canvas.create_line(350*scale, 270*scale, 350*scale, 300*scale, width=3)  # Vertikálny vodič medzi rezistormi

        resistanceText1 = self.canvas.create_text(240*scale, 270*scale, text=f"R1 = {resistance1} Ω", font=self.fontSize)
        resistanceText2 = self.canvas.create_text(420*scale, 270*scale, text=f"R2 = {resistance2} Ω", font=self.fontSize)

       
        current1Arrow = self.canvas.create_line(300*scale, 160*scale, 300*scale, 200*scale, arrow=tk.LAST, fill="red", width=4)
        current2Arrow = self.canvas.create_line(350*scale, 160*scale, 350*scale, 200*scale, arrow=tk.LAST, fill="red", width=4)
        voltageArrow = self.canvas.create_line(80*scale, 230*scale, 80*scale, 270*scale, arrow=tk.LAST, fill="green", width=4)

       
        current1Text = self.canvas.create_text(260*scale, 180*scale, text=f"I1 = 0.00 A", font=self.fontSize, fill="red")
        current2Text = self.canvas.create_text(390*scale, 180*scale, text=f"I2 = 0.00 A", font=self.fontSize, fill="red")

       
        self.canvas.create_line(350*scale, 300*scale, 50*scale, 300*scale, width=3)  # Spodný vodič k zdroju

       
        voltageLabel = tk.Label(self.canvas, text=f"Napätie: {voltage} V", font=self.fontSize, bg="white")
        voltageLabel.place(relx=0.1, rely=0.4)

        currentLabel = tk.Label(self.canvas, text=f"Prúd celkovo: {currentTotal:.2f} A", font=self.fontSize, bg="white",fg="red")
        currentLabel.place(relx=0.12, rely=0.28)

        calculateCurrents()

        
        voltageScale = tk.Scale(self.canvas, from_=1, to=24, orient="horizontal", label="Napätie (V)",border=5,bg="white", command=updateCircuit)
        voltageScale.set(voltage)
        voltageScale.place(relx=0.65, rely=0.3,relwidth=0.3,relheight=0.1)

        
        resistance1Scale = tk.Scale(self.canvas, from_=1, to=100, orient="horizontal", label="R1 (Ohm)",border=5,bg="white", command=updateCircuit)
        resistance1Scale.set(resistance1)
        resistance1Scale.place(relx=0.65, rely=0.4,relwidth=0.3,relheight=0.1)

        resistance2Scale = tk.Scale(self.canvas, from_=1, to=100, orient="horizontal", label="R2 (Ohm)",border=5,bg="white", command=updateCircuit)
        resistance2Scale.set(resistance2)
        resistance2Scale.place(relx=0.65, rely=0.5,relwidth=0.3,relheight=0.1)
#----------------------------------------------------------------------------------------------------------------------            
    def drawCircuit4(self):
        
        R = 10  
        L = 0.1  
        C = 0.001  
        U_in = 10  

        self.I_state = tk.BooleanVar(value=1)
        self.R_state = tk.BooleanVar(value=1)
        self.L_state = tk.BooleanVar(value=1)
        self.C_state = tk.BooleanVar(value=1)
        
        
        def updateCircuit():
           
            t = np.linspace(0, 0.1, 1000)
            alpha = R / (2 * L)
            omega_0 = 1 / np.sqrt(L * C)
            omega_d = np.sqrt(omega_0**2 - alpha**2) if alpha < omega_0 else 0

            if alpha < omega_0:
                # Tlmené oscilácie
                i_t = (U_in / L) * np.exp(-alpha * t) * np.sin(omega_d * t)
            else:
                # Aperiodický režim
                i_t = (U_in / L) * t * np.exp(-alpha * t)

            u_r = R * i_t
            u_l = L * np.gradient(i_t, t)
            u_c = U_in - u_r - u_l

           
            
            # Aktualizácia grafu
            ax.clear()
            ax.grid()
            if self.I_state.get() == 1:
                ax.plot(t, i_t, label="Prúd (A)")
            if self.R_state.get() == 1:
                ax.plot(t, u_r, label="Napätie na R (V)")
            if self.L_state.get() == 1:
                ax.plot(t, u_l, label="Napätie na L (V)")
            if self.C_state.get() == 1:
                ax.plot(t, u_c, label="Napätie na C (V)")
            ax.legend()
            ax.set_title("Priebeh napätia a prúdu")
            ax.set_xlabel("Čas (s)")
            ax.set_ylabel("Hodnota")
            canvas.draw()

        # Funkcia na aktualizáciu hodnôt
        def updateValues(self,*args,event=None):
            nonlocal R, L, C, U_in
            R = r_scale.get()
            L = l_scale.get()
            C = c_scale.get()
            U_in = u_scale.get()
            updateCircuit()

        # Canvas pre graf
        figure, ax = plt.subplots(figsize=(5, 4))
        ax.set_title("Priebeh napätia a prúdu")
        ax.set_xlabel("Čas (s)")
        ax.set_ylabel("Hodnota")
        canvas = FigureCanvasTkAgg(figure, master=self.canvas)
        canvasWidget = canvas.get_tk_widget()
        canvasWidget.place(relx=0.01,rely=0,relwidth=0.95,relheight=0.7)

        # Ovládacie prvky
        controlsFrame = tk.Frame(self.canvas,bg="white")
        controlsFrame.place(relx=0.2,rely=0.67,relwidth=0.8,relheight=0.32)
        
        self.I_check = tk.Checkbutton(controlsFrame,bg="white",  variable=self.I_state)
        self.I_check.place(relx=0.06,rely=0.9, relwidth=0.05,relheight=0.05)
        self.R_check = tk.Checkbutton(controlsFrame,bg="white",  variable=self.R_state)
        self.R_check.place(relx=0.06,rely=0.12, relwidth=0.05,relheight=0.05)
        self.L_check = tk.Checkbutton(controlsFrame,bg="white",  variable=self.L_state)
        self.L_check.place(relx=0.06,rely=0.33, relwidth=0.05,relheight=0.05)
        self.C_check = tk.Checkbutton(controlsFrame,bg="white",  variable=self.C_state)
        self.C_check.place(relx=0.06,rely=0.55, relwidth=0.05,relheight=0.05)
        
        self.R_state.trace_add("write", updateValues)
        self.L_state.trace_add("write", updateValues)
        self.C_state.trace_add("write", updateValues)
        self.I_state.trace_add("write", updateValues)

        tk.Label(controlsFrame, text="R (Ω):", width=20,font=self.fontSize,bg="white",justify="left").place(relx=0.1,rely=0.06,relwidth=0.12,relheight=0.15)
        r_scale = tk.Scale(controlsFrame, from_=1, to=100, orient="horizontal",border=5,bg="white", command=updateValues)
        r_scale.set(R)
        r_scale.place(relx=0.21,rely=0.02,relwidth=0.5,relheight=0.2)

        tk.Label(controlsFrame, text="L (H):",font=self.fontSize,bg="white",justify="left").place(relx=0.1,rely=0.28,relwidth=0.12,relheight=0.15)
        l_scale = tk.Scale(controlsFrame, from_=0.01, to=1, resolution=0.01, orient="horizontal",border=5,bg="white", command=updateValues)
        l_scale.set(L)
        l_scale.place(relx=0.21,rely=0.24,relwidth=0.5,relheight=0.2)

        tk.Label(controlsFrame, text="C (F):",font=self.fontSize,bg="white",justify="left").place(relx=0.1,rely=0.5,relwidth=0.12,relheight=0.15)
        c_scale = tk.Scale(controlsFrame, from_=0.0001, to=0.01, resolution=0.0001, orient="horizontal",border=5,bg="white", command=updateValues)
        c_scale.set(C)
        c_scale.place(relx=0.21,rely=0.46,relwidth=0.5,relheight=0.2)

        tk.Label(controlsFrame, text="U (V):",font=self.fontSize,bg="white",justify="left").place(relx=0.1,rely=0.71,relwidth=0.12,relheight=0.15)
        tk.Label(controlsFrame, text="I (A) ",font=self.fontSize,bg="white",justify="left").place(relx=0.1,rely=0.86,relwidth=0.12,relheight=0.15)
        u_scale = tk.Scale(controlsFrame, from_=1, to=50, orient="horizontal",border=5,bg="white", command=updateValues)
        u_scale.set(U_in)
        u_scale.place(relx=0.21,rely=0.68,relwidth=0.5,relheight=0.2)

        updateCircuit()
#----------------------------------------------------------------------------------------------------------------------        
        
    def drawCircuit5(self):
    
        N1 = 100  
        N2 = 50   
        U1 = 230  
        R = 10  

        # Funkcia na výpočet hodnôt
        def updateCircuit():
            nonlocal N1, N2, U1, R

            # Sekundárne napätie a prúd
            U2 = U1 * (N2 / N1)
            I2 = U2 / R if R != 0 else 0

            # Primárny prúd (ideálny transformátor)
            I1 = I2 * (N2 / N1)

            # Výkon
            P_in = U1 * I1
            P_out = U2 * I2

            # Aktualizácia grafu
            ax.clear()
            ax.grid()
            ax.bar(["Primárne napätie", "Sekundárne napätie"], [U1, U2], color="blue", alpha=0.7, label="Napätie (V)")
            ax.bar(["Primárny prúd", "Sekundárny prúd"], [I1, I2], color="green", alpha=0.7, label="Prúd (A)")
            ax.legend()
            ax.set_title("Ideálny transformátor: Napätie a prúd")
            canvas.draw()

            # Aktualizácia textu výkonu a ďalších informácií
            informationLabel.config(
                text=(
                    f"Vstupný výkon:         {P_in:.2f} W\n"
                    f"Výstupný výkon:       {P_out:.2f} W\n"
                    f"Primárny prúd:          {I1:.2f} A\n"
                    f"Sekundárny prúd:     {I2:.2f} A\n"
                    f"Primárne napätie:      {U1:.2f} V\n"
                    f"Sekundárne napätie: {U2:.2f} V\n"
                    f"Zaťaženie:                {R:.2f} Ω\n"
                    f"Primárne závity:        {N1}\n"
                    f"Sekundárne závity:     {N2}"
                )
            )

        # Funkcia na aktualizáciu hodnôt
        def updateValues(event=None):
            nonlocal N1, N2, U1, R
            N1 = n1_scale.get()
            N2 = n2_scale.get()
            U1 = u1_scale.get()
            R = r_load_scale.get()
            updateCircuit()

        # Canvas pre graf
        figure, ax = plt.subplots(figsize=(5, 4))
        ax.set_title("Ideálny transformátor: Napätie a prúd")
        canvas = FigureCanvasTkAgg(figure, master=self.canvas)
        canvasWidget = canvas.get_tk_widget()
        canvasWidget.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.6)

        # Ovládacie prvky
        controlsFrame = tk.Frame(self.canvas,bg="white")
        controlsFrame.place(relx=0.05,rely=0.6,relwidth=0.65,relheight=0.4)

        tk.Label(controlsFrame, text="Primárne závity (N1):",width=20, border=5,font=self.fontSize,bg="white").place(relx=0.01,rely=0.05,relwidth=0.4,relheight=0.15)
        n1_scale = tk.Scale(controlsFrame, from_=10, to=1000, orient="horizontal",border=5,bg="white",command=updateValues)
        n1_scale.set(N1)
        n1_scale.place(relx=0.41,rely=0.05,relwidth=0.3,relheight=0.2)

        tk.Label(controlsFrame, text="Sekundárne závity (N2):",font=self.fontSize,bg="white").place(relx=0.01,rely=0.25,relwidth=0.4,relheight=0.15)
        n2_scale = tk.Scale(controlsFrame, from_=10, to=1000, orient="horizontal",border=5,bg="white", command=updateValues)
        n2_scale.set(N2)
        n2_scale.place(relx=0.41,rely=0.25,relwidth=0.3,relheight=0.2)

        tk.Label(controlsFrame, text="Primárne napätie (U):",font=self.fontSize,bg="white").place(relx=0.01,rely=0.45,relwidth=0.4,relheight=0.15)
        u1_scale = tk.Scale(controlsFrame, from_=10, to=1000, orient="horizontal",border=5,bg="white", command=updateValues)
        u1_scale.set(U1)
        u1_scale.place(relx=0.41,rely=0.45,relwidth=0.3,relheight=0.2)

        tk.Label(controlsFrame, text="Zaťaženie (R):",font=self.fontSize,bg="white").place(relx=0.01,rely=0.65,relwidth=0.4,relheight=0.15)
        r_load_scale = tk.Scale(controlsFrame, from_=1, to=100, orient="horizontal",border=5,bg="white", command=updateValues)
        r_load_scale.set(R)
        r_load_scale.place(relx=0.41,rely=0.65,relwidth=0.3,relheight=0.2)

        
        informationLabel = tk.Label(self.canvas, text="", font=self.fontSize,bg="white",justify="left")
        informationLabel.place(relx=0.55,rely=0.6,relwidth=0.3,relheight=0.35)

        updateCircuit()
#----------------------------------------------------------------------------------------------------------------------        
    def drawCircuit6(self):
        scale = int(self.Cw * 0.12)
        
        vin = 12
        R1 = 10 
        R2 = 20 
        Vout = 0

        
        def calculateDivider():
            nonlocal Vout, vin, R1, R2
            try:
                vin = float(vinEntry.get())
                R1 = float(R1Entry.get())
                R2 = float(R2Entry.get())
                Vout = vin * R2 / (R1 + R2)
                
               
                self.canvas.itemconfig(vinText, text=f"Vin = {vin:.2f} V")
                self.canvas.itemconfig(R1Text, text=f"R1 = {R1:.2f} Ω")
                self.canvas.itemconfig(R2Text, text=f"R2 = {R2:.2f} Ω")
                self.canvas.itemconfig(VoutText, text=f"Vout = {Vout:.2f} V")
            except Exception as e:
                pass

        

       
        self.canvas.create_line(50*scale, 160*scale, 50*scale, 300*scale, width=3)  # Vertikálny vodič zdroja
        self.canvas.create_line(30*scale, 250*scale, 70*scale, 250*scale, width=3)  # Horný vodič zdroja
        self.canvas.create_line(40*scale, 260*scale, 60*scale, 260*scale, width=3)  # Spodný vodič zdroja

        positiveLabel = tk.Label(self.canvas, text="+", font=self.fontSize, bg="white", fg="red")
        positiveLabel.place(relx=0.04, rely=0.47)

        negativeLabel = tk.Label(self.canvas, text="-", font=self.fontSize, bg="white", fg="black")
        negativeLabel.place(relx = 0.041, rely=0.53)

        
        self.canvas.create_line(50*scale, 160*scale, 300*scale, 160*scale, width=3)  
        resistor1 = self.canvas.create_rectangle(290*scale, 230*scale, 310*scale, 270*scale, outline="black", fill="white")
        resistor2 = self.canvas.create_rectangle(290*scale, 170*scale, 310*scale, 210*scale, outline="black", fill="white")
        pin1 = self.canvas.create_oval(400*scale, 215*scale, 410*scale, 225*scale, outline="black", fill="white")
        pin2 = self.canvas.create_oval(400*scale, 295*scale, 410*scale, 305*scale, outline="black", fill="white")
        voltageArrowIn = self.canvas.create_line(80*scale, 230*scale, 80*scale, 270*scale, arrow=tk.LAST, fill="green", width=4)
        voltageArrowOut = self.canvas.create_line(405*scale, 230*scale, 405*scale, 290*scale, arrow=tk.LAST, fill="green", width=4)
        
        self.canvas.create_line(300*scale, 220*scale, 400*scale, 220*scale, width=3)  
        self.canvas.create_line(300*scale, 300*scale, 400*scale, 300*scale, width=3)  
        
        self.canvas.create_line(300*scale, 160*scale, 300*scale, 170*scale, width=3)  
        self.canvas.create_line(300*scale, 210*scale, 300*scale, 230*scale, width=3)  
        self.canvas.create_line(300*scale, 270*scale, 300*scale, 300*scale, width=3)  
        
       
        self.canvas.create_line(350*scale, 300*scale, 50*scale, 300*scale, width=3)  
    
       
        R1Text = self.canvas.create_text(355*scale, 190*scale, text=f"R1 = {R1:.2f} Ω", font=self.fontSize)    
        R2Text = self.canvas.create_text(355*scale, 250*scale, text=f"R2 = {R2:.2f} Ω", font=self.fontSize)
        VoutText = self.canvas.create_text(470*scale, 260*scale, text=f"Vout = {Vout:.2f} V", font=self.fontSize, fill="blue")
        vinText = self.canvas.create_text(140*scale, 250*scale, text=f"Vin = {vin:.2f} V", font=self.fontSize, fill="green")

       
        vinLabel = tk.Label(self.canvas, text="Vin (V):", font=self.fontSize, bg="white")
        vinLabel.place(relx=0.05, rely=0.65)
        vinEntry = tk.Entry(self.canvas,relief="solid", font=self.fontSize)
        vinEntry.insert(0, str(vin))
        vinEntry.place(relx=0.15, rely=0.65)

        R1Label = tk.Label(self.canvas, text="R1 (Ω):", font=self.fontSize, bg="white")
        R1Label.place(relx=0.05, rely=0.7)
        R1Entry = tk.Entry(self.canvas,relief="solid", font=self.fontSize)
        R1Entry.insert(0, str(R1))
        R1Entry.place(relx=0.15, rely=0.7)

        R2Label = tk.Label(self.canvas, text="R2 (Ω):", font=self.fontSize, bg="white")
        R2Label.place(relx=0.05, rely=0.75)
        R2Entry = tk.Entry(self.canvas,relief="solid", font=self.fontSize)
        R2Entry.insert(0, str(R2))
        R2Entry.place(relx=0.15, rely=0.75)

       
        calcButton = tk.Button(self.canvas, text="Vypočítaj Vout", font=self.fontSize, command=calculateDivider)
        calcButton.place(relx=0.45, rely=0.69)

        
        calculateDivider()