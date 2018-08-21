from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):

    new_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # contact_name_feature = By.ID, "com.android.contacts:id/large_title"
    contact_name_feature = By.ID, "com.android.contacts:id/cliv_name_textview"

    def click_new_contact(self):
        self.click(self.new_contact_button)

    def is_name_in_contact_name_feature(self, name):
        """
        根据姓名 查找 联系人列表中是否有这个名字
        :param name: 姓名
        :return: 是否有这个名字
        """
        # return self.find_element(self.contact_name_feature).text == name

        for i in self.find_elements(self.contact_name_feature):
            if name in i.text:
                return True
        return False
