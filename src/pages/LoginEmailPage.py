from .LoginPasswordPage import LoginPasswordPage
class LoginEmailPage():

    def __init__(self, page):
        self.page = page
        self.email_input = page.locator('#ap_email')
        self.continue_button = page.locator('input#continue')
        
    async def set_email(self, email):
        await self.email_input.fill(email)
        await self.continue_button.click()
        return LoginPasswordPage(self.page)