import sys

from runner import Runner, start_runner
from settings_handler import settings_gui, Settings


def argument_handler():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == 'settings':
            settings_gui()
            exit()
    start_runner()
    exit()
