import sys

from modules.feiertag_gui import FeiertagGUI
from modules.runner import start_runner
from modules.settings_handler import SettingsGUI


def argument_handler():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == 'settings':
            SettingsGUI().run()
            exit()
        if sys.argv[1] == 'gui':
            FeiertagGUI().run()
            exit()
    start_runner()
    exit()
