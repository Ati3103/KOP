import tkinter as tk

class VisualCircuitSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Circuit Simulator")

        # Canvas for drawing the circuit
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        # Circuit state
        self.switch_state = False  # False = Off, True = On

        # Draw circuit components
        self.draw_circuit()

    def draw_circuit(self):
        # Battery
        self.canvas.create_line(50, 150, 100, 150, width=3)  # Line from battery to switch
        self.canvas.create_text(30, 150, text="Battery", anchor="w", font=("Arial", 10))

        # Switch (open/closed)
        self.switch = self.canvas.create_line(100, 150, 150, 150, width=3)  # Initially open
        self.switch_button = self.canvas.create_oval(140, 140, 160, 160, fill="gray")
        self.canvas.tag_bind(self.switch_button, "<Button-1>", self.toggle_switch)

        # Wire to bulb
        self.canvas.create_line(150, 150, 250, 150, width=3)

        # Bulb
        self.bulb = self.canvas.create_oval(250, 130, 280, 160, fill="white", outline="black")
        self.canvas.create_text(265, 170, text="Bulb", anchor="center", font=("Arial", 10))

        # Wire back to battery
        self.canvas.create_line(280, 150, 350, 150, width=3)
        self.canvas.create_line(350, 150, 350, 50, width=3)
        self.canvas.create_line(350, 50, 50, 50, width=3)
        self.canvas.create_line(50, 50, 50, 150, width=3)

    def toggle_switch(self, event):
        # Toggle the switch state
        self.switch_state = not self.switch_state

        # Update switch and bulb visuals
        if self.switch_state:
            self.canvas.itemconfig(self.switch, fill="black")  # Switch closed
            self.canvas.itemconfig(self.bulb, fill="yellow")  # Bulb on
        else:
            self.canvas.itemconfig(self.switch, fill="white")  # Switch open
            self.canvas.itemconfig(self.bulb, fill="white")  # Bulb off


# Create application window
root = tk.Tk()
app = VisualCircuitSimulator(root)
root.mainloop()