"""
Hier befindet sich die Möglichkeiten der Einstellungen für das Programm.
Für eine einfache und ansehnliche Einstellungsmöglichkeit wird auf tkinter gesetzt als GUI.
"""
import difflib
import json
import os
from tkinter import Frame, StringVar, BooleanVar, Button, Checkbutton, Label, messagebox as mbox
from tkinter.ttk import Combobox
from tkinter import Tk, Toplevel

_bundesland_liste = [
    "Baden-Württemberg",
    "Bayern",
    "Berlin",
    "Brandenburg",
    "Bremen",
    "Hamburg",
    "Hessen",
    "Mecklenburg-Vorpommern",
    "Niedersachsen",
    "Nordrhein-Westfalen",
    "Rheinland-Pfalz",
    "Saarland",
    "Sachsen",
    "Sachsen-Anhalt",
    "Schleswig-Holstein",
    "Thüringen"
]

_file_path_settings = './data/settings.json'


class SettingsHandler:

    def __init__(self):
        if not os.path.exists(os.path.dirname(_file_path_settings)):
            os.makedirs(os.path.dirname(_file_path_settings))
        if os.path.isfile(_file_path_settings):
            with open(_file_path_settings, mode='r') as f:
                self.raw_settings = json.load(f)
        else:
            self.raw_settings = {}

    @property
    def bundesland(self):
        return self.raw_settings.get("bundesland", None)

    def set_bundesland(self, bundesland: str):
        matches = difflib.get_close_matches(bundesland, _bundesland_liste, n=1)
        if matches:
            self.raw_settings["bundesland"] = matches[0]
        else:
            if bundesland is '':
                self.remove_bundesland()
            else:
                raise ValueError('Bundesland does not exist')

    def remove_bundesland(self):
        try:
            self.raw_settings.pop("bundesland", None)
        except KeyError:
            pass

    @property
    def only_my_bundesland(self) -> bool:
        return self.raw_settings.get("only_my_bundesland", False)

    def set_only_my_bundesland(self, only_my_bundesland: bool):
        if only_my_bundesland:
            self.raw_settings["only_my_bundesland"] = True
        else:
            try:
                self.raw_settings.pop("only_my_bundesland")
            except KeyError:
                pass

    @property
    def always_running(self) -> bool:
        return self.raw_settings.get("always_running", False)

    def set_always_running(self, always_running: bool):
        if always_running:
            self.raw_settings["always_running"] = True
        else:
            try:
                self.raw_settings.pop("always_running")
            except KeyError:
                pass

    def save(self):
        if 'bundesland' not in self.raw_settings:
            try:
                self.raw_settings.pop("only_my_bundesland")
            except KeyError:
                pass
        if not os.path.exists(os.path.dirname(_file_path_settings)):
            os.makedirs(os.path.dirname(_file_path_settings))
        if len(self.raw_settings) > 0:
            with open(_file_path_settings, mode='w') as f:
                json.dump(self.raw_settings, f, indent=2, sort_keys=True)
        elif os.path.isfile(_file_path_settings):
            os.remove(_file_path_settings)


class SettingsGUI:
    def __init__(self, master=None):
        self.has_master = master is not None
        self.settings = SettingsHandler()
        self.bundesland_liste = _bundesland_liste.copy()  # Assuming this is a known list.
        self.master = master
        self.settings_window = None
        self.bundesland_entry_text = StringVar()
        self.only_my_bundesland_checkvar = BooleanVar()
        self.always_running_checkvar = BooleanVar()

    def init_window(self):
        self.settings_window = Toplevel(self.master) if self.master else Tk()
        self.settings_window.geometry("350x150")
        self.settings_window.title("Feiertagskalender Settings")
        self.settings_window.iconbitmap('./img/calender.ico')

    def init_bundesland(self):
        bundesland_frame = Frame(self.settings_window)
        bundesland_frame.pack(pady=5, padx=10)
        bundesland_label = Label(bundesland_frame, text="Mein Bundesland:")
        bundesland_label.pack(side="left")
        bundesland_combo = Combobox(bundesland_frame, value=self.bundesland_liste, textvariable=self.bundesland_entry_text)
        if self.settings.bundesland:
            bundesland_combo.set(self.settings.bundesland)
        bundesland_combo.pack(side="left")

    def init_only_my_bundesland(self):
        self.only_my_bundesland_checkvar.set(self.settings.only_my_bundesland)
        only_my_bundesland_checkbutton = Checkbutton(
            self.settings_window, text="Nur mein Bundesland berücksichtigen", variable=self.only_my_bundesland_checkvar
        )
        only_my_bundesland_checkbutton.pack(pady=5)

    def init_always_running(self):
        self.always_running_checkvar.set(self.settings.always_running)
        always_running_checkbutton = Checkbutton(
            self.settings_window, text="Programm dauerhaft laufen lassen", variable=self.always_running_checkvar
        )
        always_running_checkbutton.pack(pady=5)

    def save_settings(self):
        try:
            self.settings.set_bundesland(self.bundesland_entry_text.get())
            self.settings.set_only_my_bundesland(self.only_my_bundesland_checkvar.get())
            self.settings.set_always_running(self.always_running_checkvar.get())
            self.settings.save()
            if self.has_master:
                mbox.showinfo("Success", "Einstellungen gespeichert, zum anzeigen bitte Programm neustarten")
            else:
                mbox.showinfo("Success", "Einstellungen gespeichert")
        except ValueError as e:
            mbox.showerror("Error", str(e))

    def save_and_close(self):
        self.save_settings()
        self.settings_window.destroy()

    def init_buttons(self):
        button_frame = Frame(self.settings_window)
        button_frame.pack(pady=5, padx=10)
        save_button = Button(button_frame, text="Speichern", command=self.save_settings)
        save_button.pack(side="right", padx=5)
        save_close_button = Button(button_frame, text="Speichern & Schließen", command=self.save_and_close)
        save_close_button.pack(side="right", padx=5)

    def run(self):
        self.init_window()
        self.init_bundesland()
        self.init_only_my_bundesland()
        self.init_always_running()
        self.init_buttons()
        self.settings_window.mainloop()
