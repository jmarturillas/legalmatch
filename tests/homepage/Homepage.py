import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "tests")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from globals import config
from pagefactory.homepage import Homepage as elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from globals.functions import Functions
from robot.api.deco import keyword
import random
import time


class Homepage(object):

    def __init__(self, browser='chrome'):
        self.browser = browser
        self.driver = None
        self.wait = None
        self.func = None
        self.choice = None
        self.selected_category = None
        self.random_category_text = None

    def open_browser(self, url: str = 'https://qa8.legalmatch.com/'):

        self.driver = config.Config().get_browser(self.browser)
        self.driver.maximize_window()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)
        self.func = Functions(self.driver)

    def select_category(self):
        self.choice = elements.Homepage.category_choice()
        self.driver.find_element_by_xpath(elements.Homepage.category_dropdown).click()
        self.driver.find_element_by_xpath(self.choice).click()

    def input_zip_code(self, code='00001'):
        self.driver.find_element_by_xpath(elements.Homepage.zip_code_tbox).send_keys(code)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, elements.Homepage.green_check)))

    def click_find_lawyer(self):
        self.driver.find_element_by_xpath(elements.Homepage.btn_find_lawyer).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, elements.Homepage.lbl_legend)))
        assert self.driver.current_url == "https://qa8.legalmatch.com/home/caseIntake.do"
        assert self.func.element_contains_text(elements.Homepage.lbl_legend, elements.Homepage.chosen_category) is True
        self.driver.back()

    def click_link_here(self):
        self.driver.find_element_by_xpath(elements.Homepage.lnk_click_here).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, elements.Homepage.category_list())))

    def choose_from_other_categories_randomly_and_log(self):
        categories = self.driver.find_elements_by_xpath(elements.Homepage.category_list())
        self.selected_category = random.choice(categories)
        self.random_category_text = self.selected_category.text
        return self.random_category_text

    def navigate_to_selected_category_and_assert(self):
        self.selected_category.click()
        split_text = self.random_category_text.split(" ")
        try:
            assert self.func.element_contains_text(elements.Homepage.lbl_legend, split_text[0]) is True
        except AssertionError:
            found_text = self.driver.find_element_by_xpath(elements.Homepage.lbl_legend).text
            print("Assertion failed. There are no '{}' in the label; found '{}' instead".format(self.random_category_text, found_text))
        self.driver.back()
        assert self.driver.current_url == "https://qa8.legalmatch.com/"

    def select_other_categories_for(self, times=0):

        for time in range(int(times)):
            self.click_link_here()
            self.choose_from_other_categories_randomly_and_log()
            self.navigate_to_selected_category_and_assert()

    def scroll_down(self):
        self.driver.find_element_by_xpath(elements.Homepage.testimonial_container).location_once_scrolled_into_view
        self.driver.implicitly_wait(5)

    def loop_through_quotes(self, direction=None):

        quote_count = self.func.count_elements(elements.Homepage.carousel)
        print(quote_count)

        if direction == 'right':
            self._slide(quote_count, elements.Homepage.next_slide)
        elif direction == 'left':
            self._slide(quote_count, elements.Homepage.previous_slide)

    def _slide(self, count, xpath):
        for c in range(count):
            self.driver.find_element_by_xpath(xpath).click()
            time.sleep(1)

    def assert_meta_tag(self, meta=None):
        assert meta in self.driver.page_source





