import pytest
from helper.webuihelper import WebUITest
from selenium.webdriver.common.keys import Keys


class TestDemonstration(WebUITest):

    @pytest.mark.demo
    def test_demo(self, driver):
        self.driver.get('http://google.com')
        self.driver.find_element_by_id('lst-ib').send_keys('Kyiv Docker Meetup')
        self.driver.find_element_by_id('lst-ib').send_keys(Keys.ENTER)
        item = self.driver.find_element_by_xpath('//div[@class="g" and contains(., "Docker-Kyiv")]//div[@class="_cwc"]')
        item.find_element_by_xpath('.//a').click()
        assert self.driver.find_elements_by_xpath('//*[contains(., "Kyiv Docker Meetup #1")]')
