from jeremypy.jeremy_driver import MessengerDriver


class TestMessengerDriver(MessengerDriver):
    def __init__(self, config_file):
        super().__init__(config=config_file)

    def new_message_event(self, sender, message):
        print(f'{sender}: {message}')


if __name__ == '__main__':
    m = TestMessengerDriver(r'C:\Python Projects\Jarvis\profiles\debug\config.txt')
    m.go_to_chat()
    m.message_loop()
