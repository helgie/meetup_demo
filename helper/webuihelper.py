import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebUITest:

    @pytest.fixture
    def driver(self):
        """
        Declare self.driver value.
        :param browser: py.test fixture which returns string value taken from the sysarg '--browser' argument
        :param selenium_host: py.test fixture which returns string value taken from the sysarg '--browser' argument
        """
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=BlockCredentialedSubresources")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def find_element(self, locator, attempts=10, delay=1):
        locator, name = (locator[0], locator[1]), locator[2]
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            raise Exception('Something missing: %s' % name)

    def open(self, url):
        self.driver.get(url)

    def push(self, locator):
        self.driver.find_element(locator).click()


    def wait_for_element(self, function):
        """
        This is a decorator to wrap page open functions and to make WebDriver to wait until certain
        element is not found on the page
        :param function:
        :return:
        """
        def wrapper(locator, attempts=10, delay=2):
            """
            This is a decorator which accepts the 'locator' parameter and then looks for this element throughout
            the page for a while
            :param locator:
            :param current_url:
            :param attempts:
            :param delay:
            :return:
            """
            try:
                for attempt in range(attempts):
                    if self.driver.find_elements(locator[0], locator[1]):
                        print('found')
                        if self.driver.find_element(locator[0], locator[1]).is_displayed():
                            print('displayed')
                            return True
                        else:
                            time.sleep(delay)
                    else:
                        time.sleep(delay)
            except:
                raise Exception('Failed to find %s' % locator[2])
        return wrapper

    def wait_until_gone(self, locator, attempts=10, delay=1):
        """
        Wait until the element is not displayed
        :param locator:
        :param attempts:
        :param delay:
        """
        for attempt in range(attempts):
            if self.driver.find_elements(locator[0], locator[1]):
                if self.driver.find_element(locator[0], locator[1]).is_displayed():
                    time.sleep(delay)
                else:
                    break
            else:
                break

    def teardown_method(self, method):
        self.driver.save_screenshot('teardown.png')
        self.driver.quit()

    def is_present(self, locator):
        if self.driver.find_elements(locator[0], locator[1]):
            return True
        else:
            return False