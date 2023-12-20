import sys

from modules.runner import start_runner
from modules.settings_handler import settings_gui


def argument_handler():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == 'settings':
            settings_gui()
            exit()
    start_runner()
    exit()
