from selenium import webdriver
import unittest

class MyFirstTest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Python34\webdriver\chromedriver.exe")

    def testGoogleMail(self):
        driver = self.driver
        driver.get("https://accounts.google.com/SignUp?service=mail&continue=http%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dcarousel-about-en")

        firstNameElem = driver.find_element_by_id("FirstName")
        firstNameElem.send_keys("Анатолій")

        LastNameElem = driver.find_element_by_id("LastName")
        LastNameElem.send_keys("Миронов")

        GmailAddressElem = driver.find_element_by_id("GmailAddress")
        GmailAddressElem.send_keys("am1822608")

        PasswordElem = driver.find_element_by_name("Passwd")
        PasswordElem.send_keys ("5464546875")

        PasswdAgainElem = driver.find_element_by_name("PasswdAgain")
        PasswdAgainElem.send_keys ("5464546875")

        BirthDayElem = driver.find_element_by_name("BirthDay")
        BirthDayElem.send_keys("8")

        MonthElement = driver.find_element_by_id("month-label")
        MonthElement.click()

        MayElement = driver.find_element_by_id(":5")
        MayElement.click()

        BirthYearElem = driver.find_element_by_name("BirthYear")
        BirthYearElem.send_keys("1996")

        GenderElement = driver.find_element_by_id("Gender")
        GenderElement.click()

        GenderElement = driver.find_element_by_id(":e")
        GenderElement.click()

        RecoveryPhoneNumberElem = driver.find_element_by_name("RecoveryPhoneNumber")
        RecoveryPhoneNumberElem.send_keys("955675654")

        RecoveryEmailAddressElem = driver.find_element_by_id ("RecoveryEmailAddress")
        RecoveryEmailAddressElem.send_keys("998756754543@ukr.net")

        CountryCodeElem = driver.find_element_by_id("CountryCode")
        CountryCodeElem.click()

        CountryCodeElem = driver.find_element_by_id(":w")
        CountryCodeElem.click()

        SubmitbuttonElement = driver.find_element_by_id("submitbutton")
        SubmitbuttonElement.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()