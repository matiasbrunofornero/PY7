from .BasePage import BasePage 
from .LoginEmailPage import LoginEmailPage

class HomePage(BasePage):
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        
    async def go_to_login(self):
        await self.navigate()
        await self.click_login()
        return LoginEmailPage(self.page)