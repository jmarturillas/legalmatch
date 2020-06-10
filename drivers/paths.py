import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "drivers")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

import platform


class Paths(object):

    def __init__(self):
        self.platform = None

    def get_path_of(self, browser: str = 'chrome'):
        if browser.lower() == 'chrome':
            return Chrome().PATH
        elif browser.lower() == 'firefox':
            return Firefox().PATH


class Platform:

    @staticmethod
    def get_platform() -> str:
        if platform.system().lower() == 'darwin':
            return "macos"
        elif platform.system().lower() == 'windows':
            return "windows"
        elif platform.system().lower() == 'linux' or platform.system().lower() == 'linux2':
            return "linux"
        else:
            raise Exception("This platform is not yet supported by this framework.")


class Chrome(object):
    browser_name = 'chromedriver'

    if Platform.get_platform().lower() == 'windows':
        browser_name = 'chromedriver.exe'

    PATH = 'drivers/{platform}/{browser_name}'.format(platform=Platform.get_platform(), browser_name=browser_name)


class Firefox(object):
    browser_name = 'geckodriver'

    if Platform.get_platform().lower() == 'windows':
        browser_name = 'geckodriver.exe'

    PATH = 'drivers/{platform}/{browser_name}'.format(platform=Platform.get_platform(), browser_name=browser_name)
