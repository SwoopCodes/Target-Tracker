
## Source to remember
## Explains how to enable text field and disable again to run programatically
## https://stackoverflow.com/questions/10817917/how-to-disable-input-to-a-text-widget-but-allow-programmatic-input

import tkinter as tk

class mainwindow:

    def __init__(self):

        self.root = tk.Tk()
        
        ##
        ## Sets basic parameters  for window
        ##
        self.root.title("Target Tracker") ## sets title
        self.root.geometry("800x200") ## sets sizes
        self.root.configure(bg="#0070BB") ## sets background color

        ##
        ## Sets top headings for table
        ##
        self.targetA = tk.Label(self.root, text="Target A", font=("Arial", 18), bg="#0070BB", fg="white")
        self.targetA.grid(column=0, row=0, padx=5, pady=5,)

        self.targetB = tk.Label(self.root, text="Target B", font=("Arial", 18), bg="#0070BB", fg="white")
        self.targetB.grid(column=1, row=0, padx=10, pady=5,)

        self.targetC = tk.Label(self.root, text="Target C", font=("Arial", 18), bg="#0070BB", fg="white")
        self.targetC.grid(column=2, row=0, padx=10, pady=5,)

        self.targetD = tk.Label(self.root, text="Target D", font=("Arial", 18), bg="#0070BB", fg="white")
        self.targetD.grid(column=3, row=0, padx=10, pady=5,)

        ##
        ## Entry Field for sales target A
        ##
        self.targetAEntry = tk.Entry(self.root, font=("Arial", 14))
        self.targetAEntry.grid(column=0, row=1, padx=5, pady=5, sticky="NEWS")

        ##
        ## Text fields for calculating rest of targets
        ##
        self.targetBTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)
        self.targetBTextBox.configure(state="disabled")
        self.targetBTextBox.grid(column=1, row=1, padx=5, pady=5, sticky="NEWS")

        self.targetCTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)
        self.targetCTextBox.configure(state="disabled")
        self.targetCTextBox.grid(column=2, row=1, padx=5, pady=5, sticky="NEWS")

        self.targetDTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)
        self.targetDTextBox.configure(state="disabled")
        self.targetDTextBox.grid(column=3, row=1, padx=5, pady=5, sticky="NEWS")

        ##
        ## run button for starting calculations
        ##
        self.runButton = tk.Button(self.root, text="Run", font=("Arial", 18))
        self.runButton.grid(column=0, row=3, padx=5, pady=50, sticky="NEWS")

        ## sets area where window ends
        self.root.mainloop()

mainwindow()