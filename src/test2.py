import tkinter as tk

import tkinter as tk

class TwoWaySwitchSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Two-Way Switch Circuit Simulator")

        # Canvas for drawing the circuit
        self.canvas = tk.Canvas(root, width=500, height=300, bg="white")
        self.canvas.pack()

        # Circuit state
        self.switch1_state = False  # Switch 1: False = Position A, True = Position B
        self.switch2_state = False  # Switch 2: False = Position A, True = Position B

        # Draw the circuit
        self.draw_circuit()

    def draw_circuit(self):
        # Battery
        self.canvas.create_line(50, 150, 100, 150, width=3)  # Line from battery to switch 1
        self.canvas.create_text(30, 150, text="Battery", anchor="w", font=("Arial", 10))

        # Switch 1 (toggle positions A and B)
        self.switch1_a = self.canvas.create_line(100, 150, 150, 120, width=3)  # Position A
        self.switch1_b = self.canvas.create_line(100, 150, 150, 180, width=3)  # Position B
        self.switch1_button = self.canvas.create_oval(90, 140, 110, 160, fill="gray")
        self.canvas.tag_bind(self.switch1_button, "<Button-1>", self.toggle_switch1)

        # Switch 2 (toggle positions A and B)
        self.switch2_a = self.canvas.create_line(250, 120, 300, 150, width=3)  # Position A
        self.switch2_b = self.canvas.create_line(250, 180, 300, 150, width=3)  # Position B
        self.switch2_button = self.canvas.create_oval(240, 140, 260, 160, fill="gray")
        self.canvas.tag_bind(self.switch2_button, "<Button-1>", self.toggle_switch2)

        # Light bulb
        self.canvas.create_line(150, 120, 250, 120, width=3)  # Upper wire
        self.canvas.create_line(150, 180, 250, 180, width=3)  # Lower wire
        self.bulb = self.canvas.create_oval(350, 130, 380, 160, fill="white", outline="black")
        self.canvas.create_text(365, 170, text="Bulb", anchor="center", font=("Arial", 10))

        # Wire back to battery
        self.canvas.create_line(380, 150, 450, 150, width=3)
        self.canvas.create_line(450, 150, 450, 50, width=3)
        self.canvas.create_line(450, 50, 50, 50, width=3)
        self.canvas.create_line(50, 50, 50, 150, width=3)

        # Update circuit based on initial state
        self.update_circuit()

    def toggle_switch1(self, event):
        self.switch1_state = not self.switch1_state
        self.update_circuit()

    def toggle_switch2(self, event):
        self.switch2_state = not self.switch2_state
        self.update_circuit()

    def update_circuit(self):
        # Update switch visuals
        self.canvas.itemconfig(self.switch1_a, fill="black" if not self.switch1_state else "white")
        self.canvas.itemconfig(self.switch1_b, fill="black" if self.switch1_state else "white")
        self.canvas.itemconfig(self.switch2_a, fill="black" if not self.switch2_state else "white")
        self.canvas.itemconfig(self.switch2_b, fill="black" if self.switch2_state else "white")

        # Two-way switch logic: Light is ON if both switches are in the same position
        light_on = self.switch1_state == self.switch2_state

        # Update bulb state
        self.canvas.itemconfig(self.bulb, fill="yellow" if light_on else "white")


# Create application window
root = tk.Tk()
app = TwoWaySwitchSimulator(root)
root.mainloop()