import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_create_post():
    async with async_playwright() as playwright:
        api_request_context = await playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
        
        data = { 
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        
        response = await api_request_context.post("/posts", data=data)
        assert response.status == 201, f"Expected status code 201, but got {response.status}"

@pytest.mark.asyncio
async def test_get_post():
    async with async_playwright() as playwright:
        api_request_context = await playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
        response = await api_request_context.get("/posts/1")
        assert response.status == 200, f"Expected status code 200, but got {response.status}"
        
@pytest.mark.asyncio
async def test_update_post():
    async with async_playwright() as playwright:
        api_request_context = await playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
        
        data = { 
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        
        response = await api_request_context.put("/posts/1", data=data)
        assert response.status == 200, f"Expected status code 200, but got {response.status}"

@pytest.mark.asyncio
async def test_delete_post():
    async with async_playwright() as playwright:
        api_request_context = await playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
        response = await api_request_context.delete("/posts/1")
        assert response.status == 200, f"Expected status code 200, but got {response.status}"
