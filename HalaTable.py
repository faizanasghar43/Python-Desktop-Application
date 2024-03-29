
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pathlib
import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("500x500") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.

# Frame for TreeView
frame1 = tk.LabelFrame(root, text="Orders List")
frame1.place(height=500, width=500)

style = ttk.Style()
style.configure("Treeview",
    background = "silver",
    foreground = "black",
    rowheight = 25,
    fieldbackground = "silver" )
style.map('Treeview',
      background=[('selected', 'green')])
style.theme_use("clam")

## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = "Dummy File XYZ 11.csv"
    try:

        if file_path[-4:] == ".xlsx":
            df = pd.read_csv(file_path)
            # df = pd.read_table(file_path)
            # df = open(file_path,'rb')
        else:
            df = pd.read_csv(file_path)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None

Load_excel_data()
root.mainloop()
