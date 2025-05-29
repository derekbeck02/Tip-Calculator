# tipCalc.py
# Simple tip calculator with tkinter GUI
# By: Derek Beck

import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk
from decimal import Decimal

def calculateTip(tipPercentage, total):
    # Returns a string formatted for currency
    # tipPercentage should be formatted as an integer (ex. 15% would be 15)
    # total should be a float
 
    # Tip calculation
    tipDecimal = tipPercentage / 100 
    tip = tipDecimal * total

    # Format tip
    tip = f"{tip:.2f}"
    return tip

def calculateButtonFunction(
        inputBox,basePercentText1,basePercentText2,basePercentText3,customPercentText,customPercentPercentage,errorLabel,
        basePercentage1,basePercentage2,basePercentage3,initCustomPercentage):
    
    # Init var that will check if valid input has occured
    validInput = False
    
    # Get what the user put in the total input box into a float & check if it's a valid cash amount
    try:
        # Get user input & remove extra symbols
        inputedTotal = inputBox.get()
        inputedTotal = inputedTotal.replace("$", "")
        inputedTotal = inputedTotal.replace(",", "")
        inputedTotal = float(inputedTotal)

        # If putting the user input into a Decimal does not work, it will cause an error
        Decimal(inputedTotal)
        validInput = True

        # Reset error message
        errorLabel.configure(text = "")

        # For each tip ammount, calculate the tip
        baseTip1 = calculateTip(basePercentage1, inputedTotal)
        baseTip2 = calculateTip(basePercentage2, inputedTotal)
        baseTip3 = calculateTip(basePercentage3, inputedTotal)

    except Exception as error:        
        # Debug console print
        print(f"Total input error : {error}")
        errorLabel.configure(text = "Invalid Input. Please Try Again.")
        if inputBox.get() == "hello":
            errorLabel.configure(text = "Hello!")

    # If the calculation has happened (at least once)
    if validInput:
        # Set tip label text to the calculated tips
        basePercentText1.set(f"{basePercentage1}% : ${baseTip1}")
        basePercentText2.set(f"{basePercentage2}% : ${baseTip2}")
        basePercentText3.set(f"{basePercentage3}% : ${baseTip3}")
    
    # Custom tip amounts:
    # Get what the user put in the custom tip input box into a float & check if it's a valid percentage
    try:
        inputedCustom = customPercentPercentage.get()
        inputedCustom = inputedCustom.replace("%", "")
        inputedCustom = float(inputedCustom)
        customTip = calculateTip(inputedCustom, inputedTotal)
        customPercentText.set(f"{inputedCustom}% : ${customTip}")
    except Exception as error:
        print(f"Custom input error : {error}")
        customTip = calculateTip(initCustomPercentage, inputedTotal)
        customPercentText.set(f"{initCustomPercentage}% : ${customTip}")
    

def main():

    # Function so the tip calculations can be bound to a key
    def doCalculations(event=None):
        calculateButtonFunction(inputBox,basePercentText1,basePercentText2,basePercentText3,customPercentText,
            customPercentPercentage,errorLabel,basePercentage1,basePercentage2,basePercentage3,initCustomPercentage)
    
    # Window creation
    window = tb.Window(
        themename = "superhero",
        title = "Tip Calculator",
        iconphoto = "coin.png",
        )
    window.geometry("400x600")

    # Variables Init
    generalYPadding = 25
    mainFont = "MV_Boli"
    titleFontSize = 35
    smallFontSize = 15
    xsmallFontSize = 10
    basePercentage1 = 15
    basePercentage2 = 18
    basePercentage3 = 20
    initCustomPercentage = 25.0
    initErrorMessage = ""

    # Tk Variables Init
    totalBefore = tk.StringVar()
    basePercentText1 = tk.StringVar(value = f"{basePercentage1}% : ${basePercentage1}.00")
    basePercentText2 = tk.StringVar(value = f"{basePercentage2}% : ${basePercentage2}.00")
    basePercentText3 = tk.StringVar(value = f"{basePercentage3}% : ${basePercentage3}.00")
    customPercentPercentage = tk.StringVar()
    customPercentText = tk.StringVar(value = f"{initCustomPercentage}% : ${initCustomPercentage}.00")
    
    # Title Label
    titleLabel = ttk.Label(
        window,
        text = "Tip Calculator",
        font = f"{mainFont} {titleFontSize} bold"
    )
    titleLabel.pack(pady = generalYPadding / 2)

    # Input label
    inputLabel = ttk.Label(
        window,
        text = "Total Cost Before Tip : ",
        font = f"{mainFont} {smallFontSize} bold",
    )
    inputLabel.pack()

    # Total Before Tip Input Box
    inputBox = ttk.Entry(
        window,
        textvariable = totalBefore,
    )
    inputBox.pack(pady = generalYPadding)

    # Calculate Button
    calculateButton = ttk.Button(
        window,
        text = "Calculate",
        command = lambda : calculateButtonFunction(
            inputBox,basePercentText1,basePercentText2,basePercentText3,customPercentText,
            customPercentPercentage,errorLabel,basePercentage1,basePercentage2,basePercentage3,initCustomPercentage),
        )
    calculateButton.pack()

    # Error Label
    errorLabel = ttk.Label(
        window,
        # Placeholder text
        text = f"{initErrorMessage}",
        font = f"{mainFont} {xsmallFontSize}",
        style = "danger"
    )
    errorLabel.pack()

    # 15 Percent Label
    fifteenPercentLabel = ttk.Label(
        window,
        textvariable = basePercentText1,
        font = f"{mainFont} {smallFontSize} bold"
    )
    fifteenPercentLabel.pack(pady = generalYPadding - 10)

    # 18 Percent Label
    eighteenPercentLabel = ttk.Label(
        window,
        textvariable = basePercentText2,
        font = f"{mainFont} {smallFontSize} bold"
    )
    eighteenPercentLabel.pack(pady = generalYPadding - 10)

    # 20 Percent Label
    twentyPercentLabel = ttk.Label(
        window,
        textvariable = basePercentText3,
        font = f"{mainFont} {smallFontSize} bold"
    )
    twentyPercentLabel.pack(pady = generalYPadding - 10)

    # Custom Percent Text Label
    customPercentTextLabel = ttk.Label(
        window,
        text = "Custom Amount",
        font = f"{mainFont} {smallFontSize} bold"
    )
    customPercentTextLabel.pack(pady = generalYPadding)

    # Custom Percent Entry
    customPercentEntry = ttk.Entry(
        window,
        textvariable = customPercentPercentage,
    )
    customPercentEntry.pack()

    # Custom Percent
    customPercentLabel = ttk.Label(
        window,
        textvariable = customPercentText,
        font = f"{mainFont} {smallFontSize} bold"
    )
    customPercentLabel.pack(pady = generalYPadding)

    # Key binds
    window.bind("<Return>", doCalculations)

    # Run
    window.mainloop()

if __name__ == "__main__":
    main()