import tkinter as tk
from tkinter import messagebox, Entry, Label, Button
from database import get_table_names, get_table_columns, get_table_content, insert_into_table

listbox = None

def afisare_tabele():
    tables = get_table_names()

    root_tabele = tk.Tk()
    root_tabele.title("Numele Tabelelor")

    listbox = tk.Listbox(root_tabele)
    for table in tables:
        listbox.insert(tk.END, table)
    listbox.pack()


    def afiseaza_continut(event):
        selected_table = listbox.get(listbox.curselection()[0])
        messagebox.showinfo("Tabel selectat", "Ai selectat tabelul: {}".format(selected_table))


        afisare_formular_inserare(selected_table)

    listbox.bind('<Double-Button-1>', afiseaza_continut)


    root_tabele.mainloop()


def afisare_formular_inserare(table_name):
    columns = get_table_columns(table_name)

    root_formular = tk.Tk()
    root_formular.title("Inserare în {}".format(table_name))

    def inserare_date():
        values = [entry.get() for entry in entry_fields]
        success = insert_into_table(table_name, columns, values)

        if success:
            messagebox.showinfo("Inserare reușită", "Datele au fost introduse cu succes în tabelul {}".format(table_name))
            root_formular.destroy()
        else:
            messagebox.showerror("Eroare de inserare", "Nu s-a putut realiza inserarea în tabelul {}".format(table_name))

    entry_fields = []

    for column in columns:
        label = Label(root_formular, text=column)
        label.grid(row=columns.index(column), column=0, padx=10, pady=10)
        entry = Entry(root_formular)
        entry.grid(row=columns.index(column), column=1, padx=10, pady=10)
        entry_fields.append(entry)

    button_inserare = Button(root_formular, text="Inserare", command=inserare_date)
    button_inserare.grid(row=len(columns), column=0, columnspan=2, pady=10)

    root_formular.mainloop()

    def afiseaza_continut(event):
        selected_table = listbox.get(listbox.curselection()[0])
        messagebox.showinfo("Tabel selectat", "Ai selectat tabelul: {}".format(selected_table))


        afiseaza_fereastra_continut_tabel(selected_table)

    def afiseaza_fereastra_continut_tabel(table_name):
        root_continut_tabel = tk.Toplevel()
        root_continut_tabel.title("Continutul Tabelului: {}".format(table_name))

        frame = tk.Frame(root_continut_tabel)
        frame.pack(expand=True, fill='both')

        data = get_table_content(table_name)

        listbox = tk.Listbox(frame, selectmode='browse', font=('Courier New', 10))
        listbox.pack(expand=True, fill='both', side='left')

        scrollbar = tk.Scrollbar(frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        for row in data:
            listbox.insert('end', row)


        columns = get_table_columns(table_name)
        listbox.insert(0, " | ".join(columns))


        label_columns = tk.Label(root_continut_tabel, text=" | ".join(columns))
        label_columns.pack()


        button_inchide = tk.Button(root_continut_tabel, text="Închide", command=root_continut_tabel.destroy)
        button_inchide.pack()


        root_continut_tabel.mainloop()

