import asyncio
from playwright.async_api import async_playwright, expect
from src.pages.BasePage import BasePage
from dotenv import load_dotenv
import os
load_dotenv()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        base_page = BasePage(page)
        await base_page.navigate()

        login_email_page = await base_page.click_account_lists() 
        login_password_page = await login_email_page.set_email(os.getenv('EMAIL'))
        await login_password_page.set_password(os.getenv('PASSWORD'))
        # await page.pause() -> to handle the captcha
        
        search_results_page = await base_page.set_search("iPhone 16 Pro Max") 
        product_details_page = await search_results_page.enter_to_product_details(3)
        previous_checkout_page = await product_details_page.add_to_cart()
        checkout_page = await previous_checkout_page.go_to_checkout()
        
        page_title = await checkout_page.get_header_title()
        assert "Pago seguro" in page_title

        await browser.close()

asyncio.run(main())