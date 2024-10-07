import tkinter as tk

#-------------------------------------------------------------------------------------
root = tk.Tk()

root.attributes("-fullscreen", True)

image = tk.PhotoImage(file="background.png")
#------------------------------------------------------
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#------------------------------------------------------
tk.Label(root,  width=screen_width,height=screen_height,image=image).pack() #background
tk.Label(root, width=screen_width, height=(int((screen_height/100)*0.4)),bd=5,relief="solid", bg="gold").place(x=0, y=0)
tk.Button(root,text="X",font="Arial, 24",fg="white",bg="red",bd=5,relief="solid",width=4,command=root.destroy).place(relx=1.0, rely=0.001, anchor="ne")
#------------------------------------------------------
class TeoriaList:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrollable Button List Example")

        # Create a frame for the canvas and scrollbar
        frame = tk.Frame(root)
        frame.pack(pady=20)

        # Create a canvas to hold the buttons
        self.canvas = tk.Canvas(frame, width=300, height=200)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a vertical scrollbar linked to the canvas
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold the buttons
        self.button_frame = tk.Frame(self.canvas)

        # Create a window in the canvas to contain the button_frame
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

        # Add buttons to the button_frame
        for i in range(1, 101):
            button = tk.Button(self.button_frame, text=f"Button {i}", command=lambda i=i: self.button_action(i))
            button.pack(pady=2)  # Add some vertical space between buttons

        # Update scrollregion to encompass the button frame
        self.button_frame.update_idletasks()  # Update frame to get the correct size
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Set scroll region

    def button_action(self, button_number):
        print(f"You clicked Button {button_number}!")



scrollable_button_list = TeoriaList(root)

























root.mainloop()