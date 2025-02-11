from .LoginEmailPage import LoginEmailPage
from .SearchResultsPage import SearchResultsPage
from src.locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, page):
        self.page = page
        self.locators = BasePageLocators

    async def navigate(self):
        await self.page.goto("https://www.amazon.com")

    async def click_account_lists(self):
        await self.page.click(self.locators.ACCOUNT_LISTS_BUTTON)
        return LoginEmailPage(self.page)

    async def set_search(self, search_text):
        await self.page.fill(self.locators.SEARCH_BOX, search_text)
        await self.page.click(self.locators.SEARCH_SUBMIT)
        return SearchResultsPage(self.page)
