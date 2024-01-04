import tkinter as tk
from tkinter import Listbox, messagebox
import sqlite3

def get_table_names():
    # Conectare la baza de date
    conn = sqlite3.connect("SkyModels")
    cursor = conn.cursor()

def afisare_continut_tabel(nume_tabel):
    continut_tabel = []  # Schimbă această listă cu conținutul real al tabelului

    root_continut_tabel = tk.Toplevel()
    root_continut_tabel.title("Conținutul Tabelului: {}".format(nume_tabel))

    listbox_tabel = Listbox(root_continut_tabel)
    for row in continut_tabel:
        listbox_tabel.insert(tk.END, row)
    listbox_tabel.pack()

    def inchide_fereastra_continut_tabel():
        root_continut_tabel.destroy()

    button_inchide_continut_tabel = tk.Button(root_continut_tabel, text="Închide", command=inchide_fereastra_continut_tabel)
    button_inchide_continut_tabel.pack()

    root_continut_tabel.mainloop()

