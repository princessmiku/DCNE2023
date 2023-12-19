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
    start_runner()

