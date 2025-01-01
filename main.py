
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
        self.root.title("Target Tracker")   ## sets title
        self.root.geometry("800x200")       ## sets sizes
        self.root.configure(bg="#0070BB")   ## sets background color

        ##
        ## Sets top headings for table
        ##
        self.targetA = tk.Label(self.root, text="Target A", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## A target Heading
        self.targetA.grid(column=0, row=0, padx=5, pady=5,) ## places into window

        self.targetB = tk.Label(self.root, text="Target B", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## B target Heading
        self.targetB.grid(column=1, row=0, padx=10, pady=5,) ## places into window

        self.targetC = tk.Label(self.root, text="Target C", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## C Target Heading
        self.targetC.grid(column=2, row=0, padx=10, pady=5,) ## places into window

        self.targetD = tk.Label(self.root, text="Target D", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## D target Heading
        self.targetD.grid(column=3, row=0, padx=10, pady=5,) ## places into window

        ##
        ## Entry Field for sales target A
        ##
        self.aEntry = tk.IntVar() ## variable which takes information from Entry Label
        self.targetAEntry = tk.Entry(self.root, font=("Arial", 14),textvariable=self.aEntry) ## Creates Entry Field
        self.targetAEntry.grid(column=0, row=1, padx=5, pady=5, sticky="NEWS") ## Places into window

        ##
        ## Text fields for holding calculations of different targets
        ##
        self.targetBTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)    ## Creates text box for holding B Target
        self.targetBTextBox.configure(state="disabled")                                     ## disables ability for user to enter information
        self.targetBTextBox.grid(column=1, row=1, padx=5, pady=5, sticky="NEWS")            ## Places into window

        self.targetCTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)    ## Creates text box for holding C Target
        self.targetCTextBox.configure(state="disabled")                                     ## Disables ability for user to enter information
        self.targetCTextBox.grid(column=2, row=1, padx=5, pady=5, sticky="NEWS")            ## Places into window

        self.targetDTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)    ## Creates text box for holding D Target
        self.targetDTextBox.configure(state="disabled")                                     ## Disables ability for user to enter information
        self.targetDTextBox.grid(column=3, row=1, padx=5, pady=5, sticky="NEWS")            ## Places into window

        ##
        ## Labels for holding difference between different targets
        ##
        self.diffBoxB = tk.Label(self.root, font=("@Kozuka Mincho Pro B", 18, "bold"), text="", bg="#0070BB", fg="#3FFF00") ## Label for storing difference between A and B Target (Blank on initialisation)
        self.diffBoxB.grid(column=1, row=3, padx=0, pady=0) ## Places into window

        self.diffBoxC = tk.Label(self.root, font=("@Kozuka Mincho Pro B", 18, "bold"), text="", bg="#0070BB", fg="#3FFF00") ## Label for storing difference between B and C Target (Blank on initialisation)
        self.diffBoxC.grid(column=2, row=3, padx=0, pady=0) ## Places into window

        self.diffBoxD = tk.Label(self.root, font=("@Kozuka Mincho Pro B", 18, "bold"), text="", bg="#0070BB", fg="#3FFF00") ## Label for storing difference between C and D Target (Blank on initialisation)
        self.diffBoxD.grid(column=3, row=3, padx=0, pady=0) ## Places into window

        ##
        ## run button for starting calculations
        ##
        self.runButton = tk.Button(self.root, text="Run", font=("Arial", 18), command=self.targetCalculations) ## Creates button with on click command to begin calculations
        self.runButton.grid(column=0, row=4, padx=5, pady=10, sticky="NEWS") ## Places into window

        ## sets area where window ends
        self.root.mainloop()
    

    def targetCalculations(self): 

        ## Retrieves A target variable from window
        aTarget = self.aEntry.get()

        ## Calculates B target
        ## Formats Text
        bTarget = aTarget * 1.10
        bFormatted = f"{bTarget:,.2f}"

        ## Calculates difference between B target and A target
        ## Formats text
        bDifference = bTarget - aTarget
        bDifferenceFormatted = f"+{bDifference:,.2f}"

        ## Inputs B target into text box
        self.targetBTextBox.configure(state="normal")       ## Enables text box to allow input
        self.targetBTextBox.delete("1.0", "end")            ## Deletes previously inputted data (doesn't matter if there was none beforehand)
        self.targetBTextBox.insert("end", bFormatted)       ## Inserts B target into text box
        self.targetBTextBox.configure(state="disabled")     ## Disables text box to not allow changes by user

        ## Inputs difference into label
        self.diffBoxB.configure(text=bDifferenceFormatted)

        ## Calculates C target
        ## Formats Text
        cTarget = bTarget * 1.10
        cFormatted = f"{cTarget:,.2f}"

        ## Calculates difference between C target and B target
        ## Formats text
        cDifference = cTarget - bTarget
        cDifferenceFormatted = f"+{cDifference:,.2f}"

        ## Inputs C target into text box
        self.targetCTextBox.configure(state="normal")
        self.targetCTextBox.delete("1.0", "end")
        self.targetCTextBox.insert("end", cFormatted)
        self.targetCTextBox.configure(state="disabled")

        ## Inputs difference into label
        self.diffBoxC.configure(text=cDifferenceFormatted)

        ## Calculates D target
        ## Formats Text
        dTarget = cTarget * 1.10 
        dFormatted = f"{dTarget:,.2f}"

        ## Calculates difference between C target and B target
        ## Formats text
        dDifference = dTarget - cTarget
        dDifferenceFormatted = f"+{dDifference:,.2f}"

        ## Inputs D target into text box
        self.targetDTextBox.configure(state="normal")
        self.targetDTextBox.delete("1.0", "end") 
        self.targetDTextBox.insert("end", dFormatted)
        self.targetDTextBox.configure(state="disabled")

        ## Inputs difference into label
        self.diffBoxD.configure(text=dDifferenceFormatted)


mainwindow()