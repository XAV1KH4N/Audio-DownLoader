from Interface import Interface

class CMDInterface(Interface):

    def main(self):
        self.start()
        response = "0"

        while response != "9":
            self.menu()
            response = input(": ")

            if response == "1":
                self.downloadSong()
            elif response == "2":
                pass

    def downloadSong(self):
        title = input("Song name: ")
        try:
            self.download(title)
        except KeyboardInterrupt:
            print("Aborted Download")


    def start(self):
        print('Youtube Downloader'.center(40, '_'))

    def menu(self):
        print("1) Download Song")
        print("2) Set Download Path")
        print("9) Exit")

if __name__ == '__main__':
    cmd = CMDInterface()
    cmd.main()

