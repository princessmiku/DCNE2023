import sys
import ctypes

_myappid = 'miku.dcne2023'


def set_app_id():
    # need to display an app icon in the windows navbar...
    if sys.platform == "win32":
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(_myappid)


def setup_app():
    set_app_id()