import random
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import os
import sys

base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

class Quiz:
    def __init__(self):
            self.filename = os.path.join(base_dir, "Questions.txt")
            self.questions = []
            self.currentQuestionIndex = 0
            self.score = 0
            self.selectedQuestions = []

            self.root = tk.Tk()
            self.root.attributes("-fullscreen", True)
            
            screenWidth = self.root.winfo_screenwidth()
            screenHeight = self.root.winfo_screenheight()
            self.baseFontSize = int(min(screenWidth, screenHeight) * 0.3)
            self.fontSize = tkFont.Font(family="Arial", size=self.baseFontSize)
            
            
            closeButton = tk.Button(self.root, text="X", font="Arial 20", fg="white", bg="red",bd=5, relief="solid",  command=self.root.destroy)
            closeButton.place(relx=1.0, rely=0.001,relwidth=0.05,relheight=0.065 ,anchor="ne")
            
            self.questionLabel = tk.Label(self.root, text="",font=("Arial, 30"))
            self.questionLabel.place(relx=0.15,rely=0.2)

            self.buttons = []
            for i in range(4):
                button = tk.Button(self.root, text="", font=("Arial, 15"), width=30,relief="solid",border=5, command=lambda i=i: self.checkAnswer(i), anchor="w", justify="center")
                button.place(relx=0.2, rely=0.4 + i * 0.1, relwidth=0.6, relheight=0.08)
                self.buttons.append(button)

            self.statusLabel = tk.Label(self.root, text="", justify="center",font=("Arial, 25"))
            self.statusLabel.place(relx=0.15,rely=0.1)
            
            self.loadQuestions()
            self.startQuiz()


    def loadQuestions(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(';')
                    if len(parts) == 5: 
                        question, *answers = parts
                        correctAnswer = answers[0]  
                        self.questions.append((question, answers, correctAnswer))
        except FileNotFoundError:
            messagebox.showerror("Chyba", f"File '{self.filename}' súbor nebol nájdený.")

    def startQuiz(self):
        
        if len(self.questions) < 10:
            messagebox.showerror("Chyba", "Nedostatok otázok v súbore.")
            return

        self.selectedQuestions = random.sample(self.questions, 10)
        self.currentQuestionIndex = 0
        self.score = 0
        self.showQuestion()
        self.root.mainloop()

    def showQuestion(self):
        if self.currentQuestionIndex < len(self.selectedQuestions):
            question, answers, correctAnswer = self.selectedQuestions[self.currentQuestionIndex]

            
            self.questionLabel.config(text=f"Otázka {self.currentQuestionIndex + 1}/10: {question}")
            self.questionLabel.place(relx=0.5, rely=0.2, anchor="center")  

            
            shuffledAnswers = answers[:]
            random.shuffle(shuffledAnswers)

            prefixes = ["A", "B", "C", "D"]
            for idx, answer in enumerate(shuffledAnswers):
                self.buttons[idx].config(text=f"{prefixes[idx]}. {answer}", state=tk.NORMAL, bg="SystemButtonFace")

           
            self.correctAnswer = correctAnswer
            self.shuffledAnswers = shuffledAnswers  

            
            self.statusLabel.place(relx=0.5, rely=0.1, anchor="center")  
        else:
            self.endQuiz()

    def checkAnswer(self, idx):
        selectedAnswer = self.buttons[idx].cget("text")[3:].strip()  # Remove the A, B, C, D prefix and extra spaces
        if selectedAnswer == self.correctAnswer:
            self.score += 1
            self.statusLabel.config(text="Správne!", fg="green")
            self.buttons[idx].config(bg="lightgreen")
        else:
            self.statusLabel.config(text=f"Nesprávne! Správna odpoveď bola: {self.correctAnswer}", fg="red")
            self.buttons[idx].config(bg="lightcoral")

        for button in self.buttons:
            button.config(state=tk.DISABLED)

        self.root.after(2000, self.nextQuestion)

    def nextQuestion(self):
        
        self.statusLabel.config(text="")
        self.currentQuestionIndex += 1
        self.showQuestion()

    def endQuiz(self):
        
        messagebox.showinfo("Koniec kvízu", f"Dosiahol si {self.score}/10.")
        self.root.destroy()





