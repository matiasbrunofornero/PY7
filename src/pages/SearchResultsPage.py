from .ProductDetailsPage import ProductDetailsPage
class SearchResultsPage():

    def __init__(self, page):
        self.page = page
        self.products_list = page.locator("[role='listitem'] h2 span")
        
    async def enter_to_product_details(self, item):
        await (self.products_list.nth(item)).click()        
        return ProductDetailsPage(self.page)