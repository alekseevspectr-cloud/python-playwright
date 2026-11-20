from playwright.sync_api import Page, Locator, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page


    def fill(self, locator: Locator, text: str):
        locator.fill(text)


    def clear(self, locator: Locator):
        locator.clear()


    def click(self, locator: Locator):
        locator.click()


    def should_be_visible(self, locator: Locator):
        expect(locator).to_be_visible()


    def open(self, path: str, wait_until: str = "domcontentloaded") -> None:
        self.page.goto(path, wait_until=wait_until)