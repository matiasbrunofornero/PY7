class LoginPasswordPage():

    def __init__(self, page):
        self.page = page
        self.password_input = page.locator('#ap_password')
        self.signin_button = page.locator('#signInSubmit')
        
    async def set_password(self, password):
        await self.password_input.fill(password)
        await self.signin_button.click()
        