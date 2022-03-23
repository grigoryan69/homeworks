class Upper():
    def __init__(self, valeu):
        self.valeu = valeu

    def get_String(self):
        self.valeu = input('Enter something to go upper: ')

    def print_String(self):
        print(self.valeu.upper())

y = ""
get_upper = Upper(y)
get_upper.get_String()
get_upper.print_String()