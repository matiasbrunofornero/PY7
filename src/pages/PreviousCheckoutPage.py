from .CheckoutPage import CheckoutPage
class PreviousCheckoutPage():

    def __init__(self, page):
        self.page = page
        self.proceed_to_checkout_button = page.locator("input[name='proceedToRetailCheckout']")
        
    async def go_to_checkout(self):
        await self.proceed_to_checkout_button.click()
        return CheckoutPage(self.page)