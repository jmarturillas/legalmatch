import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "globals")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from drivers.paths import Paths
from selenium import webdriver


class Config(object):

    def __init__(self):
        self.path = Paths()
        self.driver = None

    def get_browser(self, browser: str = 'chrome'):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(_here + self.path.get_path_of(browser.lower()))
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(executable_path=_here + self.path.get_path_of(browser.lower()))
        else:
            raise Exception('This browser is not yet supported in this platform')

        return self.driver


if __name__ == '__main__':
    c = Config()
    c.get_browser('firefox')