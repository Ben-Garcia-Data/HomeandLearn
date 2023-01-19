import time
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

def database_error(err):
    messagebox.showinfo("Error", err)
    return False

def load_database_results():
    # SQL URL on the target machine is "localhost/phpmyadmin/"
    try:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              database=db_config.DB)

        sql = "SELECT * FROM tbl_employees"
        cursor = con.cursor()
        cursor.execute(sql)

        global rows
        global num_of_rows
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount

        print("# rows:", num_of_rows)

        cursor.close()
        con.close()
        has_loaded_successfully = True
        messagebox.showinfo("Connected to Database", "Connected OK")
    except pymysql.InternalError as e:
        has_loaded_successfully = database_error()
        messagebox.showinfo("Connection Error", e)
    return has_loaded_successfully

def image_path(file_path):

    open_image = Image.open(file_path)
    image = ImageTk.PhotoImage(open_image)
    return image

def load_photo_tab_one(file_path):

    image = image_path(file_path)
    imgLabelTabOne.configure(image=image)
    imgLabelTabOne.image = image

def scroll_load_data():
    fName.set(rows[row_counter][1])
    fam.set(rows[row_counter][2])
    job.set(rows[row_counter][3])
    try:

        ph_path = db_config.PHOTO_DIRECTORY + rows[row_counter][4]
        load_photo_tab_one(ph_path)

    except FileNotFoundError:

        load_photo_tab_one(db_config.PHOTO_DIRECTORY + "default.png")

def scroll_forward():

    global row_counter
    global num_of_rows
    if row_counter >= (num_of_rows - 1):
        messagebox.showinfo("Database Error", "End of database")
    else:
        row_counter = row_counter + 1
        scroll_load_data()

def scroll_back():

    global row_counter
    if row_counter == 0:
        messagebox.showinfo("Database Error", "Start of database")
    else:

        row_counter = row_counter - 1
        scroll_load_data()

def select_image():

    global image_selected
    global image_file_name
    global file_new_home
    global file_to_copy

    path_to_image = filedialog.askopenfilename(initialdir="/",
                                               title="Open File",
                                               filetypes=(("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))


# Setup
file_name = "default.png"
path = db_config.PHOTO_DIRECTORY + file_name
rows = None
num_of_rows = None
row_counter = 0
image_selected = False
image_file_name = None
file_to_copy = None
file_new_home = None

# Initialise the form
form = tk.Tk()
form.title("Tkinter Database Form")
form.geometry("500x280")

tab_parent = ttk.Notebook(form)

# Make 2 tabs & label them
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")

# Setup form variables that will be displayed inside both tabs.
fName = tk.StringVar()
fam = tk.StringVar()
job = tk.StringVar()
fNameTabTwo = tk.StringVar()
famTabTwo = tk.StringVar()
jobTabTwo = tk.StringVar()

# Assign these variables to the entry boxes.
firstEntryTabOne = tk.Entry(tab1, textvariable=fName)
familyEntryTabOne = tk.Entry(tab1, textvariable=fam)
jobEntryTabOne = tk.Entry(tab1, textvariable=job)
firstEntryTabTwo = tk.Entry(tab2, textvariable=fNameTabTwo)
familyEntryTabTwo = tk.Entry(tab2, textvariable=famTabTwo)
jobEntryTabTwo = tk.Entry(tab2, textvariable=jobTabTwo)

# The next 50 lines are pretty ugly and ideally would be cleaned up.
# === WIDGETS FOR TAB ONE
firstLabelTabOne = tk.Label(tab1, text="First Name:")
familyLabelTabOne = tk.Label(tab1, text="Family Name:")
jobLabelTabOne = tk.Label(tab1, text="Job Title:")
# ALTERNATIVELY jobLabelTabOne = tk.Label(tab1, text="Address:")
# POSSIBLE CONFLICT/TYPO HERE

imgTabOne = image_path(path)
imgLabelTabOne = tk.Label(tab1, image=imgTabOne)
imgLabelTabOne = tk.Label(tab1, image=imgTabOne)

buttonForward = tk.Button(tab1, text="Forward", command=scroll_forward)
buttonBack = tk.Button(tab1, text="Back", command=scroll_back)
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
jobLabelTabTwo = tk.Label(tab2, text="Job Title:")
# ALTERNATIVELY jobLabelTabTwo = tk.Label(tab2, text="Address:")
# AGAIN POSSIBLE TYPO

imgTabTwo = image_path(path)
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

success = load_database_results()

if success:
    fName.set(rows[row_counter][1])
    fam.set(rows[row_counter][2])
    job.set(rows[row_counter][3])
    photo_path = db_config.PHOTO_DIRECTORY + rows[row_counter][4]
    load_photo_tab_one(photo_path)

firstEntryTabOne = tk.Entry(tab1)
familyEntryTabOne = tk.Entry(tab1)
jobEntryTabOne = tk.Entry(tab1)

firstEntryTabTwo = tk.Entry(tab2)
familyEntryTabTwo = tk.Entry(tab2)
jobEntryTabTwo = tk.Entry(tab2)

tab_parent.pack(expand=1, fill='both')
form.mainloop()
