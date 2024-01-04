import tkinter as tk
from tkinter import messagebox
from database import get_user_credentials
import vizionare_tabele

def autentificare():
    username = entry_username.get()
    password = entry_parola.get()

    user = get_user_credentials(username, password)

    if user:
        messagebox.showinfo("Autentificare reușită", "Bun venit, {}".format(username))
        root.destroy()
        vizionare_tabele.afisare_tabele() 
    else:
        messagebox.showerror("Eroare de autentificare", "Credențiale incorecte")


root = tk.Tk()
root.title("Autentificare")


label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_parola = tk.Label(root, text="Parola:")
label_parola.pack()
entry_parola = tk.Entry(root, show="*")  
entry_parola.pack()


button_autentificare = tk.Button(root, text="Autentificare", command=autentificare)
button_autentificare.pack()

root.mainloop()
