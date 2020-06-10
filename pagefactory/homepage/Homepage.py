import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "pagefactory")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

import random


class Homepage(object):

    chosen_category = None

    categories = {
        "family": "Family",
        "employment": "Employment",
        "criminal_def": "Criminal Defense",
        "real_estate": "Real Estate",
        "business": "Business",
        "immigration": "Immigration",
        "personal_injury": "Personal Injury",
        "wte": "Wills, Trusts & Estates",
        "bankruptcy": "Bankruptcy & Finances",
        "government": "Government",
        "products": "Products & Services",
        "intellectual": "Intellectual Property"
    }

    category_dropdown = "//button[@data-aut='ci_add-category-dropdown']"
    zip_code_tbox = "//div/input[@data-menu-class-name='menuLocation--0']"
    green_check = "//div[@class='case-intake-form__location-checker js-case-intake-form-location-checker " \
                  "case-intake-form__location-checker--valid']"
    btn_find_lawyer = "//button[@data-aut='ci_submit-btn']"
    lbl_legend = "//legend[@data-aut='ci_chosenCat']"
    lnk_click_here = "//p/span[@data-aut='ci_otherCategories-link']"
    testimonial_container = "//div[@class='testimonials js-testimonials-home page__container page__testimonials']"
    carousel = "//div[@class='carousel-dots js-testimonials-carousel-dots']/button"
    attribute = "data-id"
    next_slide = "//div[@class='w-testimonials']/div/div/button[@aria-label='Next Slide']"
    previous_slide = "//div[@class='w-testimonials']/div/div/button[@aria-label='Previous Slide']"

    meta_tag = '<meta name="keywords" content="find a lawyer, find an attorney, find lawyers, find attorneys, legal help">'

    @staticmethod
    def category_choice(choice='Government', is_random=False):

        Homepage.chosen_category = choice

        if is_random:
            _random_choice = random.choice(list(Homepage.categories.items()))

            _choice = Homepage.categories[_random_choice[0]]

            choice = _choice
            Homepage.chosen_category = choice

        _category_choice = "//div[@class='case-intake-form__dropdown-menu dropdown-menu js-case-intake-categories-dropdown is-single-choice']/div[@data-aut='ci_add-category-list'][contains(., '{selected_category}')]".format(selected_category=choice)

        return _category_choice

    @staticmethod
    def category_list(category=''):
        category_elem = "//ul[@class='other-categories__list']/li/span[contains(., '{}')]".format(category)
        return category_elem


if __name__ == '__main__':
    # Homepage.category_choice(is_random=True)
    # print(Homepage.chosen_category)

    print(Homepage.category_list())
