import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from PIL import ImageTk, Image
import pymysql

import os
import shutil

import db_config

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "All Records":

        print("All Records tab selected")

    if tab_text == "Add New Record":

        print("Add New Record tab selected")

def load_database_results():
    try:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
    except pymysql.InternalError as e:
        messagebox.showinfo("Connection Error", e)
    return
    return

file_name = "default.png"
path = db_config.PHOTO_DIRECTORY + file_name
rows = None
num_of_rows = None

form = tk.Tk()
form.title("Tkinter Database Form")
form.geometry("500x280")



tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")

# === WIDGETS FOR TAB ONE
firstLabelTabOne = tk.Label(tab1, text="First Name:")
familyLabelTabOne = tk.Label(tab1, text="Family Name:")
jobLabelTabOne = tk.Label(tab1, text="Address:")
# ORIGINALLY jobLabelTabOne = tk.Label(tab1, text="Job Title:")
# POSSIBLE CONFLICT/TYPO HERE

firstEntryTabOne = tk.Entry(tab1)
familyEntryTabOne = tk.Entry(tab1)
jobEntryTabOne = tk.Entry(tab1)

openImageTabOne = Image.open(path)
imgTabOne = ImageTk.PhotoImage(openImageTabOne)
imgLabelTabOne = tk.Label(tab1, image=imgTabOne)

buttonForward = tk.Button(tab1, text="Forward")
buttonBack = tk.Button(tab1, text="Back")

# === END WIDGETS FOR TAB 1

# === ADD WIDGETS TO GRID ON TAB ONE
firstLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)

familyLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabOne.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

buttonBack.grid(row=3, column=0, padx=15, pady=15)
buttonForward.grid(row=3, column=2, padx=15, pady=15)

# === END ADDING WIDGETS TO GRIB FOR TAB 1

# === WIDGETS FOR TAB TWO
firstLabelTabTwo = tk.Label(tab2, text="First Name:")
familyLabelTabTwo = tk.Label(tab2, text="Family Name:")
jobLabelTabTwo = tk.Label(tab2, text="Address:")
# ORIGINALLY jobLabelTabTwo = tk.Label(tab2, text="Job Title:")
# AGAIN POSSIBLE TYPO

firstEntryTabTwo = tk.Entry(tab2)
familyEntryTabTwo = tk.Entry(tab2)
jobEntryTabTwo = tk.Entry(tab2)

openImageTabTwo = Image.open(path)
imgTabTwo = ImageTk.PhotoImage(openImageTabTwo)
imgLabelTabTwo = tk.Label(tab2, image=imgTabTwo)

buttonCommit = tk.Button(tab2, text="Add Record to Database")
buttonAddImage = tk.Button(tab2, text="Add Image")
# === END WIDGETS FOR TAB TWO
# === ADD WIDGETS TO GRID ON TAB TWO
firstLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)
imgLabelTabTwo.grid(row=0, column=2, rowspan=3, padx=15, pady=15)

familyLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)

buttonCommit.grid(row=4, column=1, padx=15, pady=15)
buttonAddImage.grid(row=4, column=2, padx=15, pady=15)
# === END ADDING WIDGETS TO GRID ON TAB TWO

tab_parent.pack(expand=1, fill='both')

form.mainloop()
