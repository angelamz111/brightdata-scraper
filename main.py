# main.py
import asyncio
from playwright.async_api import async_playwright
import os

BRIGHT_USERNAME = os.getenv("BRIGHTDATA_USERNAME")
BRIGHT_PASSWORD = os.getenv("BRIGHTDATA_PASSWORD")

TARGET_URL = "[example.com](https://example.com)"   # replace with your target

async def run():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(proxy={
            "server": "[zproxy.lum-superproxy.io](http://zproxy.lum-superproxy.io:22225)",
            "username": BRIGHT_USERNAME,
            "password": BRIGHT_PASSWORD
        })
        page = await browser.new_page()
        await page.goto(TARGET_URL)
        title = await page.title()
        print(f"Page title: {title}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
