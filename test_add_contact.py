# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.log_in(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.fill_fio(wd, firstname="Yuriy", middlename="Ivanovich", lastname="Mishin", nickname="Yesman")
        self.company_name(wd, companyname="OOO Horns and Hooves")
        self.contact_information(wd, address="Moscow City", homephone="84951231234", mobilephone="89997776655",
                            position="QA Engineer", fax="8495", main_email="pochta1@ru.ru", other_email="pochta2@ru.ru",
                            extra_email="pochta3@ru.ru")
        self.specify_the_birthday(wd, day_b="1", month_b="October", year_b="1990")
        self.specify_the_anniversary(wd, day_a="1", month_a="January", year_a="2000")
        self.selection_group(wd, select_group="dfgh")
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def selection_group(self, wd, select_group):
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(select_group)
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def specify_the_anniversary(self, wd, day_a, month_a, year_a):
        # select a day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(day_a)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        # select a month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(month_a)
        # fill a year
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(year_a)

    def specify_the_birthday(self, wd, day_b, month_b, year_b):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(day_b)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(month_b)
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(year_b)

    def contact_information(self, wd, address, homephone, mobilephone,
                            position, fax, main_email, other_email,
                            extra_email):
        # fill address
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        # fill phone numbers
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobilephone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(position)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        # fill e-mail
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(main_email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(other_email)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(extra_email)
        # fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("wwwwwww")

    def company_name(self, wd, companyname):
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(companyname)

    def fill_fio(self, wd, firstname, middlename, lastname, nickname):
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def log_in(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
