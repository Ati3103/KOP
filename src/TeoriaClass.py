import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class Teoria:
    def __init__(self, root, clearFunction, openTabs):
        self.root = root
        self.ClearFunction = clearFunction
        self.OpenList = openTabs
        self.ThemeName = ["Napätie","Prúd","Odpor","Kapacita","Induktivita","Ohmov zákon","Kirchhoffove Zákony","Vodiče"]
        

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

        scrollCanvas = tk.Canvas(panelFrame, bg="blue")
        scrollCanvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(panelFrame, orient="vertical", command=scrollCanvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.buttonContainer = tk.Frame(scrollCanvas, bg="blue")
        scrollCanvas.create_window((0, 0), window=self.buttonContainer, anchor="nw")

        scrollCanvas.configure(yscrollcommand=scrollbar.set)
        self.buttonContainer.bind("<Configure>", lambda event: scrollCanvas.configure(scrollregion=scrollCanvas.bbox("all")))
#-------------------------------------------------------------------------------------
        for Tema in self.ThemeName:
            button = tk.Button(
                self.buttonContainer,
                width=int(self.Cw * 1.2),
                text=f"{Tema}",
                relief="groove",
                bd=1,
                bg="black",
                fg="white",
                font=self.fontSize,
                command=lambda Tema=Tema: self.buttonAction(Tema)  
            )
            button.pack(pady=5, padx=3, anchor="w")
#-------------------------------------------------------------------------------------
    def buttonAction(self, button_name):
        self.ClearFunction()
        imagePath = Image.open(f"Teoria/{button_name}.png")
        resizedImage = imagePath.resize((self.ImageW, self.ImageH))
        tkImage = ImageTk.PhotoImage(resizedImage)
        imgLabel = tk.Label(self.root, image=tkImage,relief="solid")
        imgLabel.image = tkImage  
        imgLabel.place(relx=0.23,rely=0.1)  
        self.OpenList.append(imgLabel)
        
        try:
            try:
                gifPath = Image.open(f"GIF/{button_name}.gif")
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
                imagePath = Image.open(f"GIF/{button_name}.png")
                resizedImage = imagePath.resize((self.GifW, self.GifH))
                tkImage = ImageTk.PhotoImage(resizedImage)
                imgLabel = tk.Label(self.root, image=tkImage,relief="solid")
                imgLabel.image = tkImage  
                imgLabel.place(relx=0.7, rely=0.3)  
                self.OpenList.append(imgLabel)
        except (FileNotFoundError, ValueError):
            print("GIF not found or invalid.")

       
#-------------------------------------------------------------------------------------        