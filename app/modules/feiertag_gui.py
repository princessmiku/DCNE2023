import os
import webbrowser
from tkinter import Tk, Label, Frame, Menu, N, S, W, E, Scrollbar, Canvas
from tkinter import ttk
from datetime import datetime
from modules.feiertage import get_feiertage_as_list, Feiertag
from modules.settings_handler import SettingsHandler, SettingsGUI


class FeiertagGUI:
    def __init__(self):
        self.settings = SettingsHandler()
        self.feiertage: list[Feiertag] = get_feiertage_as_list()
        self.today = datetime.now().date()

        self.root = Tk()
        self.feiertag_window = None

        self.past_feiertage = [f for f in self.feiertage if f.current_year_date.date() < self.today]
        self.current_feiertage = [f for f in self.feiertage if f.current_year_date.date() == self.today]
        self.future_feiertage = [f for f in self.feiertage if f.current_year_date.date() > self.today]

    def open_settings(self):
        SettingsGUI(self.root).run()

    def open_github(self):
        webbrowser.open_new_tab('https://github.com/princessmiku/DCNE2023')

    def open_data_folder(self):
        folder_path = os.getcwd() + "/data"
        if os.path.isdir(folder_path):  # checking if the directory exists
            os.startfile(folder_path)
        else:
            os.startfile(os.getcwd())  # if the directory doesn't exist, the cwd is opened

    def setup_window(self):
        self.root.geometry("750x500")
        self.root.wm_minsize(750, 400)
        self.root.configure(bg='lightsteelblue')
        self.root.title("Feiertagskalender")
        self.root.iconbitmap('./img/calender.ico')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        general_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Allgemein", menu=general_menu)
        general_menu.add_command(label="Dateiordner öffnen", command=self.open_data_folder)
        general_menu.add_separator()
        general_menu.add_command(label="GitHub Repo", command=self.open_github)
        general_menu.add_separator()
        general_menu.add_command(label="Einstellungen", command=self.open_settings)

    def create_scrollable_area(self, parent_frame):
        canvas = Canvas(parent_frame)
        scrollbar = Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        frame_scrollable = Frame(canvas)

        canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        parent_frame.pack(fill='both', expand=True)
        return frame_scrollable

    def create_past_future_feiertag_frames(self):
        nb = ttk.Notebook(self.root)
        nb.grid(row=0, column=0, sticky=(N, S, W, E))

        past_frame = Frame(nb)
        future_frame = Frame(nb)

        past_frame_scrollable = self.create_scrollable_area(past_frame)
        future_frame_scrollable = self.create_scrollable_area(future_frame)

        nb.add(past_frame, text="Vergangene Feiertage")
        nb.add(future_frame, text="Zukünftige Feiertage")
        nb.select(1)

        return past_frame_scrollable, future_frame_scrollable

    def populate_feiertag_frames(self):
        Label(self.past_frame, text="Vergangene Feiertage:", font=('Arial', 13), fg='steelblue').pack(pady=5)
        for feiertag in self.past_feiertage:
            fg_color = 'black' if feiertag.is_for_me(self.settings.bundesland) else 'gray'
            Label(self.past_frame, text=f"{feiertag.name} war am {feiertag.current_year_date.date().strftime('%d.%m.%y')}", fg=fg_color).pack(pady=2)
        Label(self.future_frame, text="Zukünftige Feiertage:", font=('Arial', 13), fg='steelblue').pack(pady=5)
        for feiertag in self.future_feiertage:
            fg_color = 'black' if feiertag.is_for_me(self.settings.bundesland) else 'gray'
            Label(self.future_frame, text=f"{feiertag.name} wird am {feiertag.current_year_date.date().strftime('%d.%m.%y')} sein", fg=fg_color).pack(pady=2)

    def populate_current_feiertag_frame(self):
        current_frame = Frame(self.root, bg="lightsteelblue")
        current_frame.grid(column=1, row=0, sticky=(N, S, W, E), padx=20)

        Label(current_frame, text="Heutiger Feiertag:", anchor="center", font=('Arial', 15, 'bold'), bg="lightsteelblue",
              fg='steelblue').pack(pady=10)
        if len(self.current_feiertage) > 0:
            for feiertag in self.current_feiertage:
                gesetzlicher = "\nDas ist ein Gesetzlicher Feiertag bei dir im Bundesland.\n\n" if feiertag.is_for_me(self.settings.bundesland) else ""
                description_label = Label(current_frame, text=f"Heute ist {feiertag.name}\n{gesetzlicher}{feiertag.description}",
                                          font=('Arial', 12), anchor="center", bg="lightsteelblue")
                description_label.config(wraplength=300)
                description_label.pack(pady=5)
        else:
            Label(current_frame, text="Heute ist kein Feiertag", font=('Arial', 12), anchor="center", bg="lightsteelblue").pack(
                pady=5)

    def run(self):
        self.setup_window()
        self.create_menu()
        self.past_frame, self.future_frame = self.create_past_future_feiertag_frames()
        self.populate_feiertag_frames()
        self.populate_current_feiertag_frame()
        self.root.mainloop()
