from selenium import webdriver

class ChromeOptions:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()

    def get_options(self):
        self.chrome_options.add_experimental_option('detach', True)
        return self.chrome_options