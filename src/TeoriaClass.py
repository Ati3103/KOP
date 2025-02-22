import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Teoria:
    def __init__(self, root, clearFunction,removeButtonsFunction, openTabs, openButtons, removeButtons):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.RemoveButtons = removeButtonsFunction
        self.ButtonList = openButtons
        self.ThemeNames = ["Napätie","Prúd","Odpor","Výkon","Kapacita","Indukčnosť","Impedancia a Reaktancia","Frekvencia a fázový posun",
                           "Ohmov zákon","Kirchhoffove Zákony","Coulombov zákon","Elektromagnetická indukcia",
                           "Rezistor","Kondenzátor", "Tranzistor", "Cievka", "Dióda", "Transformátor",
                           "Vodiče"]
        self.ThemesWithSecondPage = ["Výkon","Tranzistor","Transformátor","Kondenzátor", "Impedancia a Reaktancia","Frekvencia a fázový posun"," Elektromagnetick8 indukcia", "Dióda", "Coulombov zákon", "Cievka"]
        self.CurrentThemeNumber = 0
        self.CurrentThemeName = "Napätie"
        self.isPage2 = False

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
 #--------       
       
        self.nextButton = tk.Button(self.root, text="Ďalej ↓",font=self.fontSize,bg="white",fg="black", border=5,relief="solid", command=lambda:(self.NextPrevious(1)))
        self.nextButton.place(relx=0.5, rely = 0.945, relwidth=0.075, relheight=0.04)
        
        self.previousButton = tk.Button(self.root, text="Naspäť ↑",font=self.fontSize,bg="white",fg="black", border=5,relief="solid", command=lambda:(self.NextPrevious(0)))
        
        self.page2button = tk.Button(self.root, text="Strana 1/2",font=self.fontSize,bg="white", border=2,relief="solid", command=lambda:(self.secondPage()))       
 #--------
        self.buttonAction("Napätie", 1)
#-------------------------------------------------------------------------------------
       
        for Theme in self.ThemeNames:
            button = tk.Button(
                self.buttonContainer,
                text=f"{Theme}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda Tema=Theme: self.buttonAction(Tema,1)  
            )
            button.pack(pady=5, padx=3, anchor="w",fill="x")
#-------------------------------------------------------------------------------------
        
            
       

    def NextPrevious(self, state):
        self.isPage2 = False
        self.page2button.config(text="Strana 1/2")
        if state == 1:
            try:
                self.buttonAction(self.ThemeNames[self.CurrentThemeNumber + 1],1)
            except:
                raise ValueError    
        if state == 0:
            try:
                self.buttonAction(self.ThemeNames[self.CurrentThemeNumber - 1],1)
            except:
                raise ValueError
    
        
    def secondPage(self):      
        self.isPage2 = not self.isPage2
        self.page2button.config(text="Strana 2/2" if self.isPage2 else "Strana 1/2")
       
        self.buttonAction(self.CurrentThemeName, 0)
            
    
            
       
    
    def buttonAction(self, buttonName, requestType):
        self.ClearFunction()
        
        
        if requestType == 1:
            self.isPage2 = False
            self.CurrentThemeNumber = self.ThemeNames.index(buttonName)
            self.CurrentThemeName = buttonName

       
        themeToLoad = self.CurrentThemeName + "2" if self.isPage2 else self.CurrentThemeName

       
        if self.CurrentThemeName in self.ThemesWithSecondPage:
            self.page2button.config(text="Strana 2/2" if self.isPage2 else "Strana 1/2")
            self.page2button.place(relx=0.22, rely=0.935, relwidth=0.1, relheight=0.06)
            self.ButtonList.append(self.page2button)
        else:
            if self.page2button.winfo_exists():
                self.page2button.place_forget()

       
        if self.CurrentThemeNumber == 0:
            if self.previousButton.winfo_exists():
                self.previousButton.place_forget()
        else:
            self.previousButton.place(relx=0.5, rely=0.08, relwidth=0.075, relheight=0.04)
            self.ButtonList.append(self.previousButton)

        
        if self.CurrentThemeNumber >= len(self.ThemeNames) - 1:
            if self.nextButton.winfo_exists():
                self.nextButton.place_forget()
        else:
            self.nextButton.place(relx=0.5, rely=0.945, relwidth=0.075, relheight=0.04)
            self.ButtonList.append(self.nextButton)

       
        try:
            imagePath = Image.open(f"Teoria/{themeToLoad}.png")
            resizedImage = imagePath.resize((self.ImageW, self.ImageH))
            tkImage = ImageTk.PhotoImage(resizedImage)
            imgLabel = tk.Label(self.root, image=tkImage, relief="solid")
            imgLabel.image = tkImage
            imgLabel.place(relx=0.22, rely=0.13)
            self.OpenList.append(imgLabel)
        except (FileNotFoundError, ValueError):
            print("No second page found.")

       
        try:
            try:
                gifPath = Image.open(f"GIF/{themeToLoad}.gif")
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
                    if gifLabel.winfo_exists():
                        gifLabel.config(image=frames[frameIndex])
                        frameIndex = (frameIndex + 1) % len(frames)
                        self.root.after(100, updateFrame)
                updateFrame()
            except Exception:
                imagePath = Image.open(f"GIF/{themeToLoad}.png")
                resizedImage = imagePath.resize((self.GifW, self.GifH))
                tkImage = ImageTk.PhotoImage(resizedImage)
                imgLabel = tk.Label(self.root, image=tkImage, relief="solid")
                imgLabel.image = tkImage
                imgLabel.place(relx=0.7, rely=0.3)
                self.OpenList.append(imgLabel)
        except (FileNotFoundError, ValueError):
            print("GIF not found or invalid.")

       
#-------------------------------------------------------------------------------------        