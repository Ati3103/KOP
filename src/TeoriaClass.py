import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from SimulatorClass import VisualCircuitSimulator


class Teoria:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.ThemeName = ["Napätie","Prúd","Odpor","Kapacita","Induktivita","Ohmov zákon","Kirchhoffove Zákony","Vodiče","x","x","x","x","x","x","x","x"]
        self.CurrentThemeNumber = 0
        self.CurrentThemeName = "Napätie"
        
        

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        baseFontSize = int(min(screenWidth, screenHeight) * 0.02)
        self.fontSize = tkFont.Font(family="Arial", size=baseFontSize)
        self.Cw = int(screenWidth/100)
        self.Ch = int(screenHeight/100)
        self.ImageW = int(screenWidth * 0.7)  
        self.ImageH = int(screenHeight * 0.8)
        self.GifW = int(screenWidth * 0.2)
        self.GifH = int(screenHeight * 0.18)
#-------------------------------------------------------------------------------------

       
        # Panel na tlačidlá s témami
        panelFrame = tk.Frame(self.root, relief="groove", bd=5, bg="blue")
        panelFrame.place(x=0, rely=0.1, relwidth=0.2, relheight=0.9)  

        # Canvas pre skrolovateľnú oblasť
        scrollCanvas = tk.Canvas(panelFrame, bg="blue", highlightthickness=0)
        scrollCanvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(panelFrame, orient="vertical", command=scrollCanvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Kontejner na tlačidlá vo vnútri Canvas
        self.buttonContainer = tk.Frame(scrollCanvas, bg="blue")
        scrollCanvas.create_window((0, 0), window=self.buttonContainer, anchor="nw")

        # Synchronizácia skrolovania
        scrollCanvas.configure(yscrollcommand=scrollbar.set)

        # Dynamická aktualizácia skrolovacej oblasti
        def update_scrollregion(event):
            scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all"))

        self.buttonContainer.bind("<Configure>", update_scrollregion)

        # Skrolovanie pomocou kolieska myši
        def on_mousewheel(event):
            scrollCanvas.yview_scroll(-1 * int(event.delta / 120), "units")

        scrollCanvas.bind_all("<MouseWheel>", on_mousewheel)
        
        nextButton = tk.Button(self.root, text="Ďalej ↓",font=self.fontSize,bg="white", border=5, command=lambda:(self.NextPrevious(1)))
        nextButton.place(relx=0.925, rely = 0.55, relwidth=0.07, relheight=0.04)
        previousButton = tk.Button(self.root, text="Naspäť ↑",font=self.fontSize,bg="white", border=5, command=lambda:(self.NextPrevious(0)))
        previousButton.place(relx=0.925, rely = 0.5, relwidth=0.07, relheight=0.04)
        
        page2button = tk.Button(self.root, text="Strana 2",font=self.fontSize,bg="white", border=5, command=lambda:(self.secondPage()))
        page2button.place(relx=0.925, rely = 0.45, relwidth=0.07, relheight=0.04)
        
#-------------------------------------------------------------------------------------
        for Theme in self.ThemeName:
            button = tk.Button(
                self.buttonContainer,
                width=int(self.Cw * 1.2),
                text=f"{Theme}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda Tema=Theme: self.buttonAction(Tema,1)  
            )
            button.pack(pady=5, padx=3, anchor="w")
#-------------------------------------------------------------------------------------
    def NextPrevious(self, state):
        if state == 1:
            try:
                self.buttonAction(self.ThemeName[self.CurrentThemeNumber + 1],1)
            except:
                raise ValueError    
        if state == 0:
            try:
                self.buttonAction(self.ThemeName[self.CurrentThemeNumber - 1],1)
            except:
                raise ValueError
        
    def secondPage(self):
        textToBeOpened = self.CurrentThemeName + "2"
        self.buttonAction(textToBeOpened,0)
        
       
    
    def buttonAction(self, buttonName, requestType):
        if requestType == 1:
            self.CurrentThemeNumber = self.ThemeName.index(buttonName)
            self.CurrentThemeName = buttonName
        self.ClearFunction()
        try:
            imagePath = Image.open(f"Teoria/{buttonName}.png")
            resizedImage = imagePath.resize((self.ImageW, self.ImageH))
            tkImage = ImageTk.PhotoImage(resizedImage)
            imgLabel = tk.Label(self.root, image=tkImage,relief="solid")
            imgLabel.image = tkImage  
            imgLabel.place(relx=0.22,rely=0.1)  
            self.OpenList.append(imgLabel)
        except(FileNotFoundError, ValueError):
            print("No second page found.")
        
        try:
            try:
                gifPath = Image.open(f"GIF/{buttonName}.gif")
                frames = [
                ImageTk.PhotoImage(gifPath.copy().resize((self.GifW, self.GifH))) 
                for frame in range(gifPath.n_frames) 
                if not gifPath.seek(frame)
                ]

                gifLabel = tk.Label(self.root, image=frames[0], relief="solid")
                gifLabel.place(relx=0.7, rely=0.3)
                self.OpenList.append(gifLabel)

                frameIndex = 0
                def updateFrame():
                        nonlocal frameIndex
                        gifLabel.config(image=frames[frameIndex])
                        frameIndex = (frameIndex + 1) % len(frames)
                        self.root.after(100, updateFrame)

                updateFrame()
            except:
                imagePath = Image.open(f"GIF/{buttonName}.png")
                resizedImage = imagePath.resize((self.GifW, self.GifH))
                tkImage = ImageTk.PhotoImage(resizedImage)
                imgLabel = tk.Label(self.root, image=tkImage,relief="solid")
                imgLabel.image = tkImage  
                imgLabel.place(relx=0.7, rely=0.3)  
                self.OpenList.append(imgLabel)
        except (FileNotFoundError, ValueError):
            print("GIF not found or invalid.")

       
#-------------------------------------------------------------------------------------        