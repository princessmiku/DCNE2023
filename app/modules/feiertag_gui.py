import os
import webbrowser
from tkinter import Tk, Label, Frame, Scrollbar, Canvas, Text, N, S, W, E, LEFT, RIGHT, Y, BOTH, Menu
from tkinter import ttk
from datetime import datetime
from tkinter.messagebox import showinfo

from modules.feiertage import get_feiertage_as_list, Feiertag
from modules.settings_handler import open_settings_gui


def open_settings(master):
    open_settings_gui(master)


def open_github():
    webbrowser.open_new_tab('https://github.com/princessmiku/DCNE2023')


def open_data_folder():
    folder_path = os.getcwd() + "/data"
    if os.path.isdir(folder_path):  # checking if the directory exists
        os.startfile(folder_path)
    else:
        os.startfile(os.getcwd())  # if the directory doesn't exist, the cwd is opened


def open_feiertag_gui():
    root = Tk()
    root.geometry("750x500")  # Modifiziert das Fenster auf größere Größe
    root.configure(bg='lightsteelblue')  # Hintergrundfarbe für ansprechendes Aussehen
    root.title("Feiertagskalender")
    root.iconbitmap('./img/calender.ico')

    # Erstellt ein "Menu" Widget
    menubar = Menu(root)
    root.config(menu=menubar)  # Fügt die Menüleiste zum Fenster hinzu

    # Fügt eine Auswahl "Einstellungen" zur Menüleiste hinzu
    general_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Allgemein", menu=general_menu)
    # Menüoptionen hinzufügen
    general_menu.add_command(label="Dateiordner öffnen", command=open_data_folder)
    general_menu.add_separator()
    general_menu.add_command(label="GitHub Repo", command=open_github)
    general_menu.add_separator()
    general_menu.add_command(label="Einstellungen", command=lambda: open_settings(root))


    feiertage: list[Feiertag] = get_feiertage_as_list()

    today = datetime(2023,8, 15).date()

    past_feiertage = [f for f in feiertage if f.current_year_date.date() < today]
    current_feiertage = [f for f in feiertage if f.current_year_date.date() == today]
    future_feiertage = [f for f in feiertage if f.current_year_date.date() > today]

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=2)
    root.grid_columnconfigure(1, weight=1)

    # Erstellt das Notebook Widget
    nb = ttk.Notebook(root)
    nb.grid(row=0, column=0, sticky=(N, S, W, E))

    # Erstellt die Rahmen für geschehene und künftige Feiertage
    past_frame = Frame(nb)
    future_frame = Frame(nb)
    nb.add(past_frame, text="Past Feiertage")
    nb.add(future_frame, text="Future Feiertage")
    nb.select(1)

    # Fuellt die Rahmen mit entsprechenden Informationen
    Label(past_frame, text="Past Feiertage:", font = ('Arial', 13), fg = 'steelblue').pack(pady=5)
    for feiertag in past_feiertage:
        Label(past_frame, text=f"{feiertag.name} was on {feiertag.current_year_date.date()}").pack(pady=2)
    Label(future_frame, text="Future Feiertage:", font = ('Arial', 13), fg = 'steelblue').pack(pady=5)
    for feiertag in future_feiertage:
        Label(future_frame, text=f"{feiertag.name} will be on {feiertag.current_year_date.date()}").pack(pady=2)

    currentFrame = Frame(root, bg="lightsteelblue")
    currentFrame.grid(column=1, row=0, sticky=(N, S, W, E), padx=20)
    Label(currentFrame, text="Today's Feiertage:", anchor="center", font = ('Arial', 15, 'bold'), bg="lightsteelblue", fg = 'steelblue').pack(pady=10)
    if len(current_feiertage) > 0:
        for feiertag in current_feiertage:
            descriptionLabel = Label(currentFrame, text=f"{feiertag.name} - {feiertag.description} is today", font = ('Arial', 12), anchor="center", bg="lightsteelblue")
            descriptionLabel.config(wraplength=300)
            descriptionLabel.pack(pady=5)
    else:
        Label(currentFrame, text="No Feiertage Today", font = ('Arial', 12), anchor="center", bg="lightsteelblue").pack(pady=5)

    root.mainloop()
