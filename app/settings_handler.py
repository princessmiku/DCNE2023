import difflib
import json
import os
import tkinter.messagebox as mbox
from tkinter import Tk, Label, StringVar, BooleanVar, Checkbutton
from tkinter import ttk, Button

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


class Settings:

    def __init__(self):
        if os.path.isfile('settings.json'):
            with open('settings.json', mode='r') as f:
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

    def save(self):
        if len(self.raw_settings) > 0:
            with open('settings.json', mode='w') as f:
                json.dump(self.raw_settings, f)
        elif os.path.isfile('settings.json'):
            os.remove('settings.json')


def settings_gui():
    root = Tk()
    root.geometry("400x200")
    root.title("Feiertagskalender Settings")

    settings = Settings()

    bundesland_label = Label(root, text="Mein Bundesland:")
    bundesland_label.pack(pady=5, padx=10)

    bundesland_entry_text = StringVar()
    bundesland_combo = ttk.Combobox(root, value=_bundesland_liste.copy(), textvariable=bundesland_entry_text)
    if settings.bundesland:
        bundesland_combo.set(settings.bundesland)
    bundesland_combo.pack(pady=5, padx=10)

    only_my_bundesland_checkvar = BooleanVar()
    only_my_bundesland_checkvar.set(settings.only_my_bundesland)
    only_my_bundesland_checkbutton = Checkbutton(
        root, text="Nur mein Bundesland berücksichtigen", variable=only_my_bundesland_checkvar
    )
    only_my_bundesland_checkbutton.pack(pady=5, padx=10)

    def save_settings():
        try:
            settings.set_bundesland(bundesland_combo.get())
            settings.set_only_my_bundesland(only_my_bundesland_checkvar.get())
            settings.save()
        except ValueError as e:
            mbox.showerror("Error", str(e))
        if settings.bundesland:
            bundesland_combo.set(settings.bundesland)

    save_button = Button(root, text="Save Settings", command=save_settings)
    save_button.pack(pady=5, padx=10)

    def save_and_close():
        save_settings()
        root.quit()

    save_close_button = Button(root, text="Save and Close Settings", command=save_and_close)
    save_close_button.pack(pady=5, padx=10)

    root.mainloop()


if __name__ == '__main__':
    settings_gui()
