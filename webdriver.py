from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Driver:
    def __init__(self):
        options = Options()
        self.instance = webdriver.Chrome()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")