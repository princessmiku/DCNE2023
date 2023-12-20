import sys

from modules.feiertag_gui import open_feiertag_gui
from modules.runner import start_runner
from modules.settings_handler import open_settings_gui


def argument_handler():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == 'settings':
            open_settings_gui()
            exit()
        if sys.argv[1] == 'gui':
            open_feiertag_gui()
            exit()
    start_runner()
    exit()
