import time

from selenium.webdriver.common.by import By

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page
import pytest



class TestContacts:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_with_file("contacts_data", "test_new_contact"))
    def test_new_contact(self, args):
        name = args["name"]
        phone= args["phone"]

        self.page.contact_list.click_new_contact()
        self.page.new_contact.click_local_save()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)
        self.page.new_contact.click_back()
        time.sleep(2)
        self.page.new_contact.press_back()
        time.sleep(2)

        assert self.page.contact_list.is_name_in_contact_name_feature(name)


