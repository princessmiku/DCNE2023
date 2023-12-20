from app_informations import set_app_id
from settings_handler import Settings


class Runner:

    def __init__(self, settings: 'Settings'):
        self.settings = settings

    def run(self):
        print()


def start_runner():
    runner = Runner(Settings())
    runner.run()


if __name__ == '__main__':
    set_app_id()
    start_runner()

