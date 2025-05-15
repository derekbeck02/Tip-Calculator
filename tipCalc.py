# tipCalc.py
# Simple tip calculator with tkinter GUI
# By: Derek Beck

import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk

def main():
    
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

    # Tk Variables Init
    totalBefore = tk.StringVar()
    fifteenPercentText = tk.StringVar()
    eighteenPercentText = tk.StringVar()
    twentyPercentText = tk.StringVar()
    customPercentPercentage = tk.StringVar()
    customPercentText = tk.StringVar()

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
        )
    calculateButton.pack()

    # 15 Percent Label
    fifteenPercentLabel = ttk.Label(
        window,
        # Placeholder text
        text = "15% : $15.00",
        font = f"{mainFont} {smallFontSize} bold"
    )
    fifteenPercentLabel.pack(pady = generalYPadding)

    # 18 Percent Label
    eighteenPercentLabel = ttk.Label(
        window,
        # Placeholder text
        text = "18% : $18.00",
        font = f"{mainFont} {smallFontSize} bold"
    )
    eighteenPercentLabel.pack()

    # 20 Percent Label
    twentyPercentLabel = ttk.Label(
        window,
        # Placeholder text
        text = "20% : $20.00",
        font = f"{mainFont} {smallFontSize} bold"
    )
    twentyPercentLabel.pack(pady = generalYPadding)

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
        # Placeholder text
        textvariable = customPercentPercentage,
    )
    customPercentEntry.pack()

    # Custom Percent
    customPercentLabel = ttk.Label(
        window,
        # Placeholder text
        text = "25% : $25.00",
        font = f"{mainFont} {smallFontSize} bold"
    )
    customPercentLabel.pack(pady = generalYPadding)

    # Run
    window.mainloop()


if __name__ == "__main__":
    main()