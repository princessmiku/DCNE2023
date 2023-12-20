import time
from datetime import datetime

from app_settings import setup_app
from modules.feiertage import get_feiertage_as_list, Feiertag
from modules.settings_handler import SettingsHandler
from notifypy import Notify


def get_default_notification() -> Notify:
    return Notify(
        default_notification_application_name="Feiertagskalender",
        default_notification_title="🕯️Es ist ein Feiertag!",
        default_notification_icon="./img/calender.ico",
        default_notification_urgency='low'
    )


_sleep_seconds = 180


class Runner:

    def __init__(self, settings: 'SettingsHandler'):
        self.settings = settings
        self.feiertage: list[Feiertag] = get_feiertage_as_list()
        self.started_at = datetime.now()

    def happy_new_year(self):
        if self.started_at.year != datetime.now().year:
            self.feiertage.clear()
            self.feiertage = get_feiertage_as_list()
            self.started_at = datetime.now()

    def loop_feiertage(self):
        self.happy_new_year()
        for feiertag in self.feiertage:
            if feiertag.current_year_date.date() != datetime.now().date():
                continue
            if self.settings.only_my_bundesland and not feiertag.is_for_me(self.settings.bundesland):
                continue
            notification = get_default_notification()

            notification.title = f"🕯 Heute ist {feiertag.name}"

            msg = ""
            if (self.settings.bundesland and feiertag.is_for_me(self.settings.bundesland)) or feiertag.is_global:
                msg += "🙂 Dieser Feiertag wird in deinem Bundesland gefeiert.\n"

            notification.message = msg
            notification.send()
            self.feiertage.remove(feiertag)

    def run(self):
        self.loop_feiertage()
        while self.settings.always_running:
            # time.sleep ist sehr effizient da es zu der Zeit dann keine systemleistung nutzt
            time.sleep(_sleep_seconds)
            self.loop_feiertage()


def start_runner():
    runner = Runner(SettingsHandler())
    runner.run()


if __name__ == '__main__':
    setup_app()
    start_runner()
