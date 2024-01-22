# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Yuriy")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Ivanovich")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Mishin")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Yesman")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Title123")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("OOO Horns and Hooves")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow City")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("84951231234")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("89997776655")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("QA Engineer")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("8495")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("pochta1@ru.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("pochta2@ru.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("pochta3@ru.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("wwwwwww")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("dfgh")
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
