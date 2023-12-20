# need to display an app icon in the windows navbar...
import ctypes

_myappid = 'miku.dcne2023'


def set_app_id():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(_myappid)

