import pytest
from helper.webuihelper import WebUITest

from selenium.webdriver.common.keys import Keys


class TestDemonstration(WebUITest):

    @pytest.mark.demo
    def test_demo(self, driver):
        self.driver.get('http://google.com')
        self.driver.find_element_by_id('lst-ib').send_keys('Kyiv Docker meetup  ')
        self.driver.find_element_by_id('lst-ib').send_keys(Keys.ENTER)
        item = self.driver.find_element_by_xpath('//div[@class="g" and contains(., "Docker-Kyiv")]//h3/a')
        item.click()
        assert self.driver.find_elements_by_xpath('//*[contains(., "Kyiv Docker Meetup #2")]')
