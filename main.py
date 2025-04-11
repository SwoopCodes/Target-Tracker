
import tkinter as tk

class mainwindow:

    def __init__(self):

        self.root = tk.Tk()
        
        ##
        ## Sets basic parameters  for window
        ##
        self.root.title("Target Calculator")   ## sets title
        self.root.geometry("600x200")       ## sets sizes
        self.root.configure(bg="#0070BB")   ## sets background color

        ##
        ## Sets top headings for table
        ##
        self.targetA = tk.Label(self.root, text="SAP Target", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## A target Heading
        self.targetA.grid(column=0, row=0, padx=5, pady=5,) ## places into window

        self.targetB = tk.Label(self.root, text="Target A", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## B target Heading
        self.targetB.grid(column=1, row=0, padx=10, pady=5,) ## places into window

        self.targetC = tk.Label(self.root, text="Target B", font=("@Kozuka Mincho Pro B", 18, "bold"), bg="#0070BB", fg="white") ## C Target Heading
        self.targetC.grid(column=2, row=0, padx=10, pady=5,) ## places into window

        ##
        ## Entry Field for SAP Target
        ##
        self.SAPEntry = tk.IntVar() ## variable which takes information from Entry Label
        self.SAPTargetEntry = tk.Entry(self.root, font=("Arial", 14),textvariable=self.SAPEntry) ## Creates Entry Field
        self.SAPTargetEntry.grid(column=0, row=1, padx=5, pady=5, sticky="NEWS") ## Places into window

        ##
        ## Text fields for holding calculations of different targets
        ##
        self.targetATextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)    ## Creates text box for holding A Target
        self.targetATextBox.configure(state="disabled")                                     ## disables ability for user to enter information
        self.targetATextBox.grid(column=1, row=1, padx=5, pady=5, sticky="NEWS")            ## Places into window

        self.targetBTextBox = tk.Text(self.root, font=("Arial", 14), height=1, width=15)    ## Creates text box for holding B Target
        self.targetBTextBox.configure(state="disabled")                                     ## Disables ability for user to enter information
        self.targetBTextBox.grid(column=2, row=1, padx=5, pady=5, sticky="NEWS")            ## Places into window

        ##
        ## run button for starting calculations
        ##
        self.runButton = tk.Button(self.root, text="Run", font=("Arial", 18), command=self.targetCalculations) ## Creates button with on click command to begin calculations
        self.runButton.grid(column=0, row=4, padx=5, pady=10, sticky="NEWS") ## Places into window

        ## sets area where window ends
        self.root.mainloop()
    

    def targetCalculations(self): 

        ## Retrieves SAP target variable from window
        SAPTarget = self.SAPEntry.get()

        ## Calculates A target
        ## Formats Text
        ATarget = SAPTarget / 1.33
        AFormatted = f"{ATarget:,.2f}"

        ## Inputs A target into text box
        self.targetATextBox.configure(state="normal")       ## Enables text box to allow input
        self.targetATextBox.delete("1.0", "end")            ## Deletes previously inputted data (doesn't matter if there was none beforehand)
        self.targetATextBox.insert("end", AFormatted)       ## Inserts B target into text box
        self.targetATextBox.configure(state="disabled")     ## Disables text box to not allow changes by user

        ## Calculates B target
        ## Formats Text
        BTarget = ATarget * 1.10
        BFormatted = f"{BTarget:,.2f}"

        ## Inputs B target into text box
        self.targetBTextBox.configure(state="normal")
        self.targetBTextBox.delete("1.0", "end")
        self.targetBTextBox.insert("end", BFormatted)
        self.targetBTextBox.configure(state="disabled")


mainwindow()