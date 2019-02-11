"""
User enters a number and sees the quote related to that number.
"""

quotes = ('A man is not complete until he is married. Then he is '
          'finished.', 'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted women.', 'Black'
          ' holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not Found!'
        return value


class QuoteTerminalView:
    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                index = self.view.select_quote()
                index = int(index)
                valid_input = True
            except ValueError:
                self.view.error("Incorrect Index: '{}'".format(index))
        quote = self.model.get_quote(index)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
