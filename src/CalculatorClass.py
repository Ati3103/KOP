import tkinter as tk
import tkinter.font as tkFont
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io
import math



class Calculator:
    def __init__(self, root, clearFunction, openTabs):
#-------------------------------------------------------------------------------------
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.OperationName = ["Ohmov zákon","Výkon","Odpor vodiča","Kapacita","Indukčnosť Cievky"]
        
        
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        self.baseFontSize = int(min(screenWidth, screenHeight) * 0.02)
        self.fontSize = tkFont.Font(family="Arial", size=self.baseFontSize)
        self.valueBaseFontSize = int(min(screenWidth, screenHeight) * 0.025)
        self.valueFontSize = tkFont.Font(family="Arial", size=self.valueBaseFontSize)
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
        for Formula in self.OperationName:
            button = tk.Button(
                self.buttonContainer,
                width=int(self.Cw * 1.2),
                text=f"{Formula}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda Formula=Formula: self.buttonAction(Formula)  
            )
            button.pack(pady=5, padx=3, anchor="w")
#-------------------------------------------------------------------------------------
        
    def buttonAction(self, button_name):
        if button_name == "Ohmov zákon":
                self.CalculateOhmsLaw() 
        elif button_name == "Výkon":
                self.CalculatePower()
        elif button_name == "Odpor vodiča":
                self.CalculateWireResistance() 
        elif button_name == "Indukčnosť Cievky":
                self.CalculateInduction()   
        elif button_name == "Kapacita":
            self.CalculateCapacity()    
#-------------------------------------------------------------------------------------    
    def CalculateOhmsLaw(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root,bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.8)
        self.OpenList.append(frame)
      
        self.entryR = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryR.place(relx=0.25,rely=0.01)
        self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryU.place(relx=0.25,rely=0.08)
        self.entryI = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryI.place(relx=0.25,rely=0.15)
        
        self.labelR = tk.Label(frame,text="R [Ω]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelR.place(relx=0.07,rely=0.01)
        self.labelU = tk.Label(frame,text="U [V]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelU.place(relx=0.07,rely=0.08)
        self.labelI = tk.Label(frame,text="I  [A]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelI.place(relx=0.07,rely=0.15)

        
        self.Result = tk.Label(frame, text=f"Výsledok: {self.result} ",font=self.fontSize,bg="DeepSkyBlue4",fg="white")
        self.Result.place(relx=0.13,rely=0.25,relwidth=0.7,relheight=0.15)

        formula = r"$U = I \cdot R$         $I = \frac{U}{R}$           $R = \frac{U}{I}$"

        def createFormulaImage(formula):
            fig, ax = plt.subplots()
            
            ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize,ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)
        formulaImage = createFormulaImage(formula)
        
        self.Info = tk.Label(frame, image=formulaImage,font=self.fontSize,bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Info.place(x=0, rely=0.6,relwidth=1,relheight=0.3)
        
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
                    self.result = "Nevhodné hodnoty"
            except ValueError:
                self.result = "Nevhodné hodnoty"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
#-------------------------------------------------------------------------------------   
    def CalculatePower(self):
            self.ClearFunction()
            self.result = 0
            frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
            frame.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.8)
            self.OpenList.append(frame)
        
            self.entryR = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryR.place(relx=0.25,rely=0.01)
            self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryU.place(relx=0.25,rely=0.08)
            self.entryI = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryI.place(relx=0.25,rely=0.15)
            
            self.labelR = tk.Label(frame,text="P [W]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelR.place(relx=0.07,rely=0.01)
            self.labelU = tk.Label(frame,text="U [V]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelU.place(relx=0.07,rely=0.08)
            self.labelI = tk.Label(frame,text="I  [A]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelI.place(relx=0.07,rely=0.15)

            
            self.Result = tk.Label(frame, text=f"Výsledok: P = {self.result} W",font=self.fontSize,bg="DeepSkyBlue4",fg="white")
            self.Result.place(relx=0.13,rely=0.25,relwidth=0.7,relheight=0.15)

            formula = r"$P = I^2 \cdot R$         $P = \frac{U^2}{R}$           $P = I \cdot U$"

            def create_formula_image(formula):
                fig, ax = plt.subplots()
                ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize,ha='center', va='center')
                ax.axis('off')

                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                plt.close(fig)
                buf.seek(0)

                img = Image.open(buf)
                return ImageTk.PhotoImage(img)
            
            formulaImage = create_formula_image(formula)
            
            self.Info = tk.Label(frame, image=formulaImage,font=self.fontSize,bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
            self.Info.place(x=0, rely=0.6,relwidth=1,relheight=0.3)
            
            def Calculate():
                R = self.entryR.get()
                U = self.entryU.get()
                I = self.entryI.get()

                try:
                    R = float(R) if R else None
                    U = float(U) if U else None
                    I = float(I) if I else None

                    
                    if U is not None and I is not None and R is None:
                        self.result = (f"{U * I} W")
                    elif I is not None and R is not None and U is None:
                        self.result = (f"{I**2 * R} W")
                    elif U is not None and R is not None and I is None:
                        self.result = (f"{(U**2)/R} W") 
                    else:
                        self.result = "Nevhodné hodnoty"
                except ValueError:
                    self.result = "Nevhodné hodnoty"

            
                self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

            
            self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
            self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
    #-------------------------------------------------------------------------------------    
    def CalculateWireResistance(self):
            self.ClearFunction()
            self.result = 0
            frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
            frame.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.8)
            self.OpenList.append(frame)

            self.isCopper = tk.BooleanVar()
            self.isAluminium = tk.BooleanVar()
            
            self.entryl = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryl.place(relx=0.25,rely=0.01)
            self.entryA = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryA.place(relx=0.25,rely=0.08)
            self.Copper = tk.Checkbutton(frame, text="Meď", font=self.fontSize, variable=self.isCopper )
            self.Copper.place(relx=0.35, rely = 0.2)
            self.Aluminium = tk.Checkbutton(frame, text="Hliník", font=self.fontSize, variable=self.isAluminium)
            self.Aluminium.place(relx=0.45, rely = 0.2)
            
            self.labell = tk.Label(frame,text="l [m]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labell.place(relx=0.07,rely=0.01)
            self.labelA = tk.Label(frame,text="A [mm2]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelA.place(relx=0.07,rely=0.08)
            self.labelMaterial = tk.Label (frame, text="Materiál vodiča",font=self.valueFontSize, fg="white", bg="DeepSkyBlue4")
            self.labelMaterial.place(relx=0.07, rely=0.2)
            

            
            self.Result = tk.Label(frame, text=f"Výsledok: R = {self.result} Ω",font=self.fontSize,bg="DeepSkyBlue4",fg="white")
            self.Result.place(relx=0.13,rely=0.25,relwidth=0.7,relheight=0.15)

            formula = r"$R = ρ\cdot \frac{l}{A}$"

            def create_formula_image(formula):
                fig, ax = plt.subplots()
                ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize,ha='center', va='center')
                ax.axis('off')

                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                plt.close(fig)
                buf.seek(0)

                img = Image.open(buf)
                return ImageTk.PhotoImage(img)
            
            formulaImage = create_formula_image(formula)
            
            self.Info = tk.Label(frame, image=formulaImage,font=self.fontSize,bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
            self.Info.place(x=0, rely=0.6,relwidth=1,relheight=0.3)
            
            def Calculate():
                l = self.entryl.get()
                A = self.entryA.get()
                ρ1 = self.isCopper.get()
                ρ2 = self.isAluminium.get()
                ρ = None

                try:
                    
                    l = float(l) if l else None
                    A = float(A) if A else None
                    
                    
                    if ρ1 == 1 and ρ2 == 0:
                        ρ = 1.68e-8  
                    elif ρ1 == 0 and ρ2 == 1:       
                        ρ = 2.7e-8  
                    else:
                        ρ = None  

                    
                    if l is not None and A is not None and ρ is not None:
                        print(f"Length: {l}, Area: {A}, Resistivity: {ρ}")
                        
                        resistance = ρ * (l / (A * 1e-6))
                        self.result = f"{resistance:.6f} Ω"  
                    else:
                        self.result = "Nevhodné hodnoty"
                except ValueError:
                      self.result = "Nevhodné hodnoty"

            
                self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

            
            self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
            self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
    #-------------------------------------------------------------------------------------    
    def CalculateInduction(self):
            self.ClearFunction()
            self.result = 0
            frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
            frame.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.8)
            self.OpenList.append(frame)
           
            self.entryN = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryN.place(relx=0.25,rely=0.01)
            self.entryl = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryl.place(relx=0.25,rely=0.08)
            self.entryA = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryA.place(relx=0.25,rely=0.15)
            self.entryμr = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
            self.entryμr.place(relx=0.25, rely=0.22)
            
            self.labelN = tk.Label(frame,text="N [z]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelN.place(relx=0.07,rely=0.01)
            self.labell = tk.Label(frame,text="l [m]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labell.place(relx=0.07,rely=0.08)
            self.labelA = tk.Label(frame,text="A [mm2]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelA.place(relx=0.07,rely=0.15)
            self.labelμr = tk.Label(frame,text="μr ",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelμr.place(relx=0.07,rely=0.22)
            
    
            self.Result = tk.Label(frame, text=f"Výsledok: L = {self.result} H",font=self.fontSize,bg="DeepSkyBlue4",fg="white")
            self.Result.place(relx=0.13,rely=0.3,relwidth=0.7,relheight=0.15)

            formula = r"$L = μ\cdot \frac{N^2\cdot A}{l}$"

            def create_formula_image(formula):
                fig, ax = plt.subplots()
                ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize,ha='center', va='center')
                ax.axis('off')

                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                plt.close(fig)
                buf.seek(0)

                img = Image.open(buf)
                return ImageTk.PhotoImage(img)
            
            formulaImage = create_formula_image(formula)
            
            self.Info = tk.Label(frame, image=formulaImage,font=self.fontSize,bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
            self.Info.place(x=0, rely=0.6,relwidth=1,relheight=0.3)
            
            def Calculate():
                N = self.entryN.get()
                l = self.entryl.get()
                A = self.entryA.get()
                μr = self.entryμr.get()

                try:
                    
                    N = int(N) if N else None  
                    A = float(A) if A else None  
                    l = float(l) if l else None  
                    μr = float(μr) if μr else None 
                    
                   
                    μ0 = 4 * math.pi * 1e-7  

                    if μr is not None:
                        μ0 = μ0 * μr
                    else:
                        μ0 = None  

                   
                    if N is not None and A is not None and l is not None and μ0 is not None:
                        
                        A_m2 = A * 1e-6  
                        inductance = μ0 * (N**2) * (A_m2 / l)
                        self.result = f"{inductance:.6e} H"  
                    else:
                        self.result = "Nevhodné hodnoty"
                except ValueError:
                        self.result = "Nevhodné hodnoty"
            
                self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

            
            self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
            self.StartButton.place(relx=0.33,rely=0.45,relwidth=0.3,relheight=0.1)
    #-------------------------------------------------------------------------------------    
    def CalculateCapacity(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root,bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.8)
        self.OpenList.append(frame)
      
        self.entryC = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryC.place(relx=0.25,rely=0.01)
        self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryU.place(relx=0.25,rely=0.08)
        self.entryQ = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4")
        self.entryQ.place(relx=0.25,rely=0.15)
        
        self.labelC = tk.Label(frame,text="C [F]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelC.place(relx=0.07,rely=0.01)
        self.labelU = tk.Label(frame,text="U [V]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelU.place(relx=0.07,rely=0.08)
        self.labelQ = tk.Label(frame,text="Q  [C]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.labelQ.place(relx=0.07,rely=0.15)

        
        self.Result = tk.Label(frame, text=f"Výsledok: {self.result} ",font=self.fontSize,bg="DeepSkyBlue4",fg="white")
        self.Result.place(relx=0.13,rely=0.25,relwidth=0.7,relheight=0.15)

        formula = r"$C = \frac{Q}{U}$           $U = \frac{Q}{C}$          $Q = C \cdot U$"

        def createFormulaImage(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize,ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)
        formulaImage = createFormulaImage(formula)
        
        self.Info = tk.Label(frame, image=formulaImage,font=self.fontSize,bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")
        self.Info.place(x=0, rely=0.6,relwidth=1,relheight=0.3)
        
        def Calculate():
            C = self.entryC.get()
            U = self.entryU.get()
            Q = self.entryQ.get()

            try:
                C = float(C) if C else None
                U = float(U) if U else None
                Q = float(Q) if Q else None

                if C is None and U is not None and Q is not None:
                    self.result = (f"{Q / U} F")
                elif U is None and C is not None and Q is not None:
                    self.result = (f"{Q / C} V")
                elif Q is None and C is not None and U is not None:
                    self.result = (f"{U * C} C")
                else:
                    self.result = "Nevhodné hodnoty"
            except ValueError:
                self.result = "Nevhodné hodnoty"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
#-------------------------------------------------------------------------------------   