from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements_by_xpath("//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)