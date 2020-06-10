import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "globals")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))


class Functions(object):

    def __init__(self, driver=None):
        self.driver = driver

    def click_element(self, elem=None):
        pass

    def element_contains_text(self, element=None, text=None) -> bool:
        extracted_text = self.driver.find_element_by_xpath(element).text

        if text in extracted_text:
            return True
        else:
            return False

    def count_elements(self, element) -> int:
        count = len(self.driver.find_elements_by_xpath(element))
        return count
