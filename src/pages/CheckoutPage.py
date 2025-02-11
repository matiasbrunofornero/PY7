class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.header_title = page.locator("#nav-checkout-title-header-text")
        
    async def get_header_title(self):
        return await self.header_title.inner_text()
