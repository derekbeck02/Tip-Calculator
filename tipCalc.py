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
        iconphoto = "coin.png")
    window.geometry("500x600")

    # Variables Init
    totalBefore = tk.StringVar()

    # Input label
    inputLabel = ttk.Label(
        text = "Total Cost Before Tip : ",
        font = "MV_Boli 25 bold"
    )
    inputLabel.pack()

    # Total Before Tip Input Box
    inputBox = ttk.Entry(
        window,
        textvariable = totalBefore,
    )
    
    # Run
    window.mainloop()


if __name__ == "__main__":
    main()