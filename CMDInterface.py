from Interface import Interface

class CMDInterface(Interface):

    def main(self):
        self.start()
        response = "0"

        while response != "9":
            self.menu()
            response = input(": ")

            if response == "1":
                pass
            elif response == "2":
                pass

    def start(self):
        print('Youtube Downloader'.center(40, '_'))

    def menu(self):
        print("1) Download Song")
        print("2) Set Download Path")
        print("9) Exit")
