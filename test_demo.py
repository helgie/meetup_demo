import pytest, time
from helper.webuihelper import WebUITest
from selenium.webdriver.common.keys import Keys


class TestDemonstration(WebUITest):

    @pytest.mark.demo
    def test_demo(self, driver):
        self.driver.get('http://google.com')
        self.driver.find_element_by_id('lst-ib').send_keys('Kyiv Docker Meetup')
        self.driver.find_element_by_id('lst-ib').send_keys(Keys.ENTER)
        time.sleep(5)