from selenium import webdriver


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser: use 'chrome' or 'firefox'")
