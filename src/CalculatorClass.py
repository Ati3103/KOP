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
        self.OperationName = ["Ohmov zákon","Výkon","Odpor vodiča","Kapacita","Indukčnosť Cievky", "Sériovo zapojené: R/C", "Paralelne zapojené: R/C", ]
        
        
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
        
        
        self.CalculateOhmsLaw()
        self.themeName = tk.Label(self.root,text="Ohmov zákon",font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
        self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
        self.OpenList.append(self.themeName)
#-------------------------------------------------------------------------------------
        for Formula in self.OperationName:
            button = tk.Button(
                self.buttonContainer,
                text=f"{Formula}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda Formula=Formula: self.buttonAction(Formula)  
            )
            button.pack(pady=5, padx=3, anchor="w", fill="x")
#-------------------------------------------------------------------------------------
        
        

    def buttonAction(self, buttonName):
        if buttonName == "Ohmov zákon":
                self.CalculateOhmsLaw()
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Výkon":
                self.CalculatePower()
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Odpor vodiča":
                self.CalculateWireResistance() 
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Indukčnosť Cievky":
                self.CalculateInduction() 
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Kapacita":
                self.CalculateCapacity()
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Sériovo zapojené: R/C":   
                self.CalculateSerial()
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
        elif buttonName == "Paralelne zapojené: R/C":   
                self.CalculateParallel()  
                self.themeName = tk.Label(self.root,text=buttonName,font=self.valueFontSize,fg="white", bg="DeepSkyBlue4",bd=5, relief="solid")
                self.themeName.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
                self.OpenList.append(self.themeName)
            
#-------------------------------------------------------------------------------------   
        
    def CalculateOhmsLaw(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root,bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(relx=0.3,rely=0.2,relwidth=0.5,relheight=0.8)
        self.OpenList.append(frame)
        
      
        self.entryR = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryR.place(relx=0.25,rely=0.01)
        self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryU.place(relx=0.25,rely=0.08)
        self.entryI = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryI.place(relx=0.25,rely=0.15)
        
        self.label1 = tk.Label(frame,text="R [Ω]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.label1.place(relx=0.07,rely=0.01)
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
                    self.result = "Chyba, zadajte všetky hodnoty správne"
            except ValueError:
                self.result = "Chyba, zadajte všetky hodnoty správne"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
#-------------------------------------------------------------------------------------   
    def CalculatePower(self):
            self.ClearFunction()
            self.result = 0
            frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
            frame.place(relx=0.3,rely=0.2,relwidth=0.5,relheight=0.8)
            self.OpenList.append(frame)
        
            self.entryR = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entryR.place(relx=0.25,rely=0.01)
            self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entryU.place(relx=0.25,rely=0.08)
            self.entryI = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entryI.place(relx=0.25,rely=0.15)
            
            self.label1 = tk.Label(frame,text="P [W]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.label1.place(relx=0.07,rely=0.01)
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
                        self.result = "Chyba, zadajte všetky hodnoty správne"
                except ValueError:
                    self.result = "Chyba, zadajte všetky hodnoty správne"

            
                self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

            
            self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
            self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
    #-------------------------------------------------------------------------------------    
    def CalculateWireResistance(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root, width=int(self.Cw * 70), height=int(self.Ch * 25), bg="DeepSkyBlue4", bd=5, relief="solid")
        frame.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.8)
        self.OpenList.append(frame)

        

        
        self.entry1 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry1.place(relx=0.35, rely=0.01)
        self.entry2 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry2.place(relx=0.35, rely=0.08)
        self.entryρ = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entryρ.place(relx=0.35, rely=0.15)

        self.isR = tk.BooleanVar()
        self.isC = tk.BooleanVar()
        
        self.R = tk.Checkbutton(frame, text="Meď",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isR)
        self.R.place(relx=0.35, rely=0.22)
        self.C = tk.Checkbutton(frame, text="Hliník",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isC)
        self.C.place(relx=0.45, rely=0.22)

        self.label1 = tk.Label(frame, text="l [m]", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label1.place(relx=0.15, rely=0.01)
        self.label2 = tk.Label(frame, text="A [mm²]", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label2.place(relx=0.15, rely=0.08)
        self.labelMaterial = tk.Label(frame, text="ρ", font=self.valueFontSize, fg="white", bg="DeepSkyBlue4")
        self.labelMaterial.place(relx=0.15, rely=0.15)
        
        self.Result = tk.Label(frame, text=f"Výsledok: R = {self.result} Ω", font=self.fontSize, bg="DeepSkyBlue4", fg="white")
        self.Result.place(relx=0.13, rely=0.3, relwidth=0.7, relheight=0.15)
        
        
        def updateEntry(Material, *args):
            if self.isR.get() and not self.isC.get():
                self.entryρ.delete(0, tk.END)
                self.entryρ.insert(0, "1.68e-8")  
                self.isC.set(False)
            elif self.isC.get() and not self.isR.get():
                self.entryρ.delete(0, tk.END)
                self.entryρ.insert(0, "2.7e-8") 
                self.isR.set(False)
            elif not self.isC.get() and not self.isR.get():
                self.entryρ.delete(0, tk.END)
            elif self.isC.get() and self.isR.get():
                if Material == "Copper":
                    self.entryρ.delete(0, tk.END)
                    self.entryρ.insert(0, "1.68e-8")  
                    self.isC.set(False)
                elif Material == "Aluminium":
                    self.entryρ.delete(0, tk.END)
                    self.entryρ.insert(0, "2.7e-8") 
                    self.isR.set(False)
                else:
                    self.entryρ.delete(0, tk.END)
                      
       
        self.isR.trace_add("write", lambda *args:updateEntry("Copper"))
        self.isC.trace_add("write", lambda*args:updateEntry("Aluminium"))

       
        formula = r"$R = ρ\cdot \frac{l}{A}$"

       
        def createFormulaImage(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize, ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)

        formulaImage = createFormulaImage(formula)

      
        self.Info = tk.Label(frame, image=formulaImage, font=self.fontSize, bg="DeepSkyBlue4", fg="white", bd=2, relief="solid")
        self.Info.place(x=0, rely=0.6, relwidth=1, relheight=0.3)

       
        def Calculate():
            l = self.entry1.get()
            A = self.entry2.get()
            ρ = self.entryρ.get()

            try:
                l = float(l) if l else None
                A = float(A) if A else None
                ρ = float(ρ) if ρ else None

                
                if l is not None and A is not None and ρ is not None:
                    resistance = ρ * (l / (A * 1e-6))  
                    self.result = f"{resistance:.6f} Ω"
                else:
                    self.result = "Chyba, zadajte všetky hodnoty správne"  

            except ValueError:
                self.result = "Chyba, zadajte všetky hodnoty správne"  

            
            self.Result.config(text=f"Výsledok: {self.result}", bg="DeepSkyBlue4", fg="white")

       
        self.StartButton = tk.Button(frame, text="Vypočítať", font=self.fontSize, bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33, rely=0.45, relwidth=0.3, relheight=0.1)

        
        
    #-------------------------------------------------------------------------------------    
    def CalculateInduction(self):
            self.ClearFunction()
            self.result = 0
            frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
            frame.place(relx=0.3,rely=0.2,relwidth=0.5,relheight=0.8)
            self.OpenList.append(frame)
           
            self.entryN = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entryN.place(relx=0.25,rely=0.01)
            self.entry1 = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entry1.place(relx=0.25,rely=0.08)
            self.entry2 = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entry2.place(relx=0.25,rely=0.15)
            self.entryμr = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
            self.entryμr.place(relx=0.25, rely=0.22)
            
            self.labelN = tk.Label(frame,text="N [z]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.labelN.place(relx=0.07,rely=0.01)
            self.label1 = tk.Label(frame,text="l [m]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.label1.place(relx=0.07,rely=0.08)
            self.label2 = tk.Label(frame,text="A [mm2]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
            self.label2.place(relx=0.07,rely=0.15)
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
                l = self.entry1.get()
                A = self.entry2.get()
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
                        self.result = "Chyba, zadajte všetky hodnoty správne"
                except ValueError:
                        self.result = "Chyba, zadajte všetky hodnoty správne"
            
                self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

            
            self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
            self.StartButton.place(relx=0.33,rely=0.45,relwidth=0.3,relheight=0.1)
    #-------------------------------------------------------------------------------------    
    def CalculateCapacity(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root,bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(relx=0.3,rely=0.2,relwidth=0.5,relheight=0.8)
        self.OpenList.append(frame)
      
        self.entryC = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryC.place(relx=0.25,rely=0.01)
        self.entryU = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryU.place(relx=0.25,rely=0.08)
        self.entryQ = tk.Entry(frame,font=self.valueFontSize,bg="DeepSkyBlue4", fg="white")
        self.entryQ.place(relx=0.25,rely=0.15)
        
        self.label2 = tk.Label(frame,text="C [F]",font=self.valueFontSize,bg="DeepSkyBlue4",fg="white")
        self.label2.place(relx=0.07,rely=0.01)
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
                    self.result = "Chyba, zadajte všetky hodnoty správne"
            except ValueError:
                self.result = "Chyba, zadajte všetky hodnoty správne"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font=self.fontSize,bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33,rely=0.4,relwidth=0.3,relheight=0.1)
#-------------------------------------------------------------------------------------   
    def CalculateSerial(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root, width=int(self.Cw * 70), height=int(self.Ch * 25), bg="DeepSkyBlue4", bd=5, relief="solid")
        frame.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.8)
        self.OpenList.append(frame)

        

        
        self.entry1 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry1.place(relx=0.35, rely=0.01)
        self.entry2 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry2.place(relx=0.35, rely=0.08)
    
        self.isR = tk.BooleanVar()
        self.isC = tk.BooleanVar()
        
        self.R = tk.Checkbutton(frame, text="Rezistor",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isR)
        self.R.place(relx=0.25, rely=0.22)
        self.C = tk.Checkbutton(frame, text="Kondenzátor",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isC)
        self.C.place(relx=0.45, rely=0.22)

        self.label1 = tk.Label(frame, text="", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label1.place(relx=0.15, rely=0.01)
        self.label2 = tk.Label(frame, text="", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label2.place(relx=0.15, rely=0.08)
        
        self.Result = tk.Label(frame, text=f"Výsledok: R = {self.result} Ω", font=self.fontSize, bg="DeepSkyBlue4", fg="white")
        self.Result.place(relx=0.13, rely=0.3, relwidth=0.7, relheight=0.15)
        
        
        def updateEntry(Component, *args):
            if self.isR.get() and not self.isC.get():
                self.label1.config(text="R1 [Ω]")
                self.label2.config(text="R2 [Ω]") 
                self.Result.config(text=f"Výsledok: R = 0 Ω")
                self.isC.set(False)
            elif self.isC.get() and not self.isR.get():
                self.label1.config(text="C1 [F]")
                self.label2.config(text="C2 [F] ") 
                self.Result.config(text=f"Výsledok: C = 0 F")
                self.isR.set(False)
            elif self.isC.get() and self.isR.get():
                if Component == "R":
                    self.label1.config(text="R1 [Ω]")
                    self.label2.config(text="R2 [Ω]")
                    self.Result.config(text=f"Výsledok: R = 0 Ω")   
                    self.isC.set(False)
                elif Component == "C":
                    self.label1.config(text="C1 [F]")
                    self.label2.config(text="C2 [F]") 
                    self.Result.config(text=f"Výsledok: C = 0 F")
                    self.isR.set(False)
                else:
                    pass
                      
       
        self.isR.trace_add("write", lambda *args:updateEntry("R"))
        self.isC.trace_add("write", lambda*args:updateEntry("C"))

       
        formula = r"""  R = R1 + R2  
        
$C = \frac{C1\cdot C2}{C2 + C1}$"""

       
        def createFormulaImage(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize, ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)

        formulaImage = createFormulaImage(formula)

      
        self.Info = tk.Label(frame, image=formulaImage, font=self.fontSize, bg="DeepSkyBlue4", fg="white", bd=2, relief="solid")
        self.Info.place(x=0, rely=0.6, relwidth=1, relheight=0.3)

       
        def Calculate():
            val1 = self.entry1.get()
            val2 = self.entry2.get()
           

            try:
                val1 = float(val1) if val1 else None
                val2 = float(val2) if val2 else None
               

                
                if val1 is not None and val2 is not None:
                    if self.isR.get():
                        print("R it is")
                        result = (val1 + val2) 
                        print(result) 
                        self.result = f"R = {result} Ω"
                    elif self.isC.get() == True:
                        result = (val1 * val2) / (val1 + val2)
                        self.result = f"C = {result} F"
                else:
                    self.result = "Zadajte všetky potrebné hodnoty správne"  

            except ValueError:
                self.result = "Chyba, zadajte všetky hodnoty správne"  

            
            self.Result.config(text=f"Výsledok: {self.result}", bg="DeepSkyBlue4", fg="white")

       
        self.StartButton = tk.Button(frame, text="Vypočítať", font=self.fontSize, bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33, rely=0.45, relwidth=0.3, relheight=0.1)
#---------------------------------------------------------------------------------------------------------------------------
    def CalculateParallel(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root, width=int(self.Cw * 70), height=int(self.Ch * 25), bg="DeepSkyBlue4", bd=5, relief="solid")
        frame.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.8)
        self.OpenList.append(frame)

        

        
        self.entry1 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry1.place(relx=0.35, rely=0.01)
        self.entry2 = tk.Entry(frame, font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.entry2.place(relx=0.35, rely=0.08)
    
        self.isR = tk.BooleanVar()
        self.isC = tk.BooleanVar()
        
        self.R = tk.Checkbutton(frame, text="Rezistor",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isR)
        self.R.place(relx=0.25, rely=0.22)
        self.C = tk.Checkbutton(frame, text="Kondenzátor",bg="DeepSkyBlue4", font=self.fontSize, variable=self.isC)
        self.C.place(relx=0.45, rely=0.22)

        self.label1 = tk.Label(frame, text="", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label1.place(relx=0.15, rely=0.01)
        self.label2 = tk.Label(frame, text="", font=self.valueFontSize, bg="DeepSkyBlue4", fg="white")
        self.label2.place(relx=0.15, rely=0.08)
        
        self.Result = tk.Label(frame, text=f"Výsledok: R = {self.result} Ω", font=self.fontSize, bg="DeepSkyBlue4", fg="white")
        self.Result.place(relx=0.13, rely=0.3, relwidth=0.7, relheight=0.15)
        
        
        def updateEntry(Component, *args):
            if self.isR.get() and not self.isC.get():
                self.label1.config(text="R1 [Ω]")
                self.label2.config(text="R2 [Ω]") 
                self.Result.config(text=f"Výsledok: R = 0 Ω")
                self.isC.set(False)
            elif self.isC.get() and not self.isR.get():
                self.label1.config(text="C1 [F]")
                self.label2.config(text="C2 [F] ") 
                self.Result.config(text=f"Výsledok: C = 0 F")
                self.isR.set(False)
            elif self.isC.get() and self.isR.get():
                if Component == "R":
                    self.label1.config(text="R1 [Ω]")
                    self.label2.config(text="R2 [Ω]")
                    self.Result.config(text=f"Výsledok: R = 0 Ω")   
                    self.isC.set(False)
                elif Component == "C":
                    self.label1.config(text="C1 [F]")
                    self.label2.config(text="C2 [F]") 
                    self.Result.config(text=f"Výsledok: C = 0 F")
                    self.isR.set(False)
                else:
                    pass
            else:
                self.result = "Vyberte súčiastku"
                      
       
        self.isR.trace_add("write", lambda *args:updateEntry("R"))
        self.isC.trace_add("write", lambda*args:updateEntry("C"))

       
        formula = r"""  C = C1 + C2  
        
$R = \frac{R1\cdot R2}{R2 + R1}$"""

       
        def createFormulaImage(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=self.valueBaseFontSize, ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)

        formulaImage = createFormulaImage(formula)

      
        self.Info = tk.Label(frame, image=formulaImage, font=self.fontSize, bg="DeepSkyBlue4", fg="white", bd=2, relief="solid")
        self.Info.place(x=0, rely=0.6, relwidth=1, relheight=0.3)

       
        def Calculate():
            val1 = self.entry1.get()
            val2 = self.entry2.get()
           

            try:
                val1 = float(val1) if val1 else None
                val2 = float(val2) if val2 else None
               

                
                if val1 is not None and val2 is not None:
                    if self.isC.get():
                        result = (val1 + val2) 
                        self.result = f"C = {result} F"
                    elif self.isR.get() == True:
                        result = (val1 * val2) / (val1 + val2)
                        self.result = f"R = {result} Ω"
                else:
                    self.result = "Zadajte všetky potrebné hodnoty správne"  

            except ValueError:
                self.result = "Chyba, zadajte všetky hodnoty správne"  

            
            self.Result.config(text=f"Výsledok: {self.result}", bg="DeepSkyBlue4", fg="white")

       
        self.StartButton = tk.Button(frame, text="Vypočítať", font=self.fontSize, bd=2, relief="solid", command=Calculate)
        self.StartButton.place(relx=0.33, rely=0.45, relwidth=0.3, relheight=0.1)
