from .PreviousCheckoutPage import PreviousCheckoutPage
class ProductDetailsPage():

    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-button")
        
    async def add_to_cart(self):
        await self.add_to_cart_button.click()        
        return PreviousCheckoutPage(self.page)