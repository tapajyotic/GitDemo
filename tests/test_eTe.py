import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.CheckOut import CheckOutPage
from pageObjects.HomePage import Home
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = Home(self.driver)
        homePage.shopItems().click()
        #shopButton = self.driver.find_element_by_css_selector("a[href*='shop']")
        #self.driver.execute_script("arguments[0].click();", shopButton)
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        checkoutpage = CheckOutPage.getCardTitle()

        for pdt in checkoutpage:
            pdtName = pdt.find_element_by_xpath("div/h4/a").text
            if pdtName == "Blackberry":
                pdt.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()

        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Success" in self.driver.find_element_by_css_selector("div[class*='alert-dismissible']").text

        self.driver.get_screenshot_as_file("screen1.png")



