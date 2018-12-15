import configparser


class Config:
    hostname = ""
    env = ""

    def __init__(self):
        # set some default
        self.hostname = "https://xyz.cit.api.here.com/"
        self.env = "cit"

    def load(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.hostname = config['env']['hostname']
            self.env = config['env']['name']
        except:
            print("Error loading")
