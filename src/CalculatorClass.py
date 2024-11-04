import tkinter as tk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io



class Calculator:
    def __init__(self, root, clearFunction, openTabs):
        #-------------------------------------------------------------------------------------
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.NazovOperacie = {"Ohmov zákon","Výkon"}
        
        
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)

        frame = tk.Frame(root,relief="groove",bd=5,bg="blue")
        frame.place(x=0,y=self.Ch*10)  
 
        self.canvas = tk.Canvas(frame, width=self.Cw*20, height=self.Ch*80, bg="lightblue")
        self.canvas.pack(side="left", fill="both", expand=True)
   
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
    
        self.button_frame = tk.Frame(self.canvas)
      
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")
        #-------------------------------------------------------------------------------------
        for i in self.NazovOperacie:
            button = tk.Button(self.button_frame, text=f"{i}", relief="groove",bd=1, bg="black",fg="white", width=int(self.Cw*1.82),height=int(self.Ch*0.2)
                               ,font=("Arial, 15") ,command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  

        self.button_frame.update_idletasks()  
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  
        #-------------------------------------------------------------------------------------
        
    def button_action(self, button_name):
       if button_name == "Ohmov zákon":
            self.CalculateOhmsLaw() 
       elif button_name == "Výkon":
            self.CalculatePower()            
#-------------------------------------------------------------------------------------    
    def CalculateOhmsLaw(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(x=self.Cw*30, y=self.Ch*30)
        self.OpenList.append(frame)
      
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
        self.Result.place(x=470, y=120)

        formula = r"$U = I \cdot R$         $I = \frac{U}{R}$           $R = \frac{U}{I}$"

        def create_formula_image(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=28,ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)
        formulaImage = create_formula_image(formula)
        
        self.Info = tk.Label(frame, image=formulaImage,font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid",width=self.Cw*38,height=self.Ch*10)
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
                    self.result = "Nevhodné hodnoty"
            except ValueError:
                self.result = "Nevhodné hodnoty"

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")

        
        self.StartButton = tk.Button(frame, text="Vypočítať",font="Arial, 15",bd=2, relief="solid", command=Calculate)
        self.StartButton.place(x=150, y=150)
#-------------------------------------------------------------------------------------   
    def CalculatePower(self):
        self.ClearFunction()
        self.result = 0
        frame = tk.Frame(self.root, width=int(self.Cw*70), height=int(self.Ch*25),bg="DeepSkyBlue4",bd=5, relief="solid")
        frame.place(x=self.Cw*30, y=self.Ch*30)
        self.OpenList.append(frame)
      
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
        self.Result.place(x=470, y=120)

        formula = r"$P = I^2 \cdot R$         $P = \frac{U^2}{R}$           $P = I \cdot U$"

        def create_formula_image(formula):
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, formula, fontsize=24,ha='center', va='center')
            ax.axis('off')

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)

            img = Image.open(buf)
            return ImageTk.PhotoImage(img)
        
        formulaImage = create_formula_image(formula)
        
        self.Info = tk.Label(frame, image=formulaImage,font=("Arial, 30"),bg="DeepSkyBlue4",fg="white",bd=2, relief="solid",width=self.Cw*38,height=self.Ch*10)
        self.Info.place(x=470, y=20)
        
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

           
            self.Result.config(text=f"Výsledok: {self.result}",bg="DeepSkyBlue4",fg="white",bd=2, relief="solid")

        # Button to trigger calculation
        self.StartButton = tk.Button(frame, text="Vypočítať",font="Arial, 15",bd=2, relief="solid", command=Calculate)
        self.StartButton.place(x=150, y=150)
#-------------------------------------------------------------------------------------    
