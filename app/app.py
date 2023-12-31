"""
Feiertagskalender

Der Feiertagskalender zeigt dir alle kommenden Feiertage der Nächsten Zeit.
Dazu zeigt er dir diese auch noch entsprechend den Bundesländern an.

Funktionen
- Kalender
- Feiertage anzeigen
- Benachrichtigen aktuellen sowie kommenden Feiertagen
- Kleiner bereich mit Einstellungen zur Personalisierung

Der Kalender läuft unter der MIT License
"""
from app_settings import setup_app
from modules.argument_handler import argument_handler


if __name__ == '__main__':
    setup_app()
    argument_handler()
