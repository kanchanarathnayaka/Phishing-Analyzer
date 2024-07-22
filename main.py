import asyncio
from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.staticfiles import StaticFiles
=======
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d
from pydantic import BaseModel
from typing import List
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
<<<<<<< HEAD
import base64
import time
from fastapi.openapi.utils import get_openapi

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
=======
import sys
import base64
from fastapi.openapi.utils import get_openapi
import yaml

app = FastAPI()
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d

class URLItem(BaseModel):
    url: str

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    return html_content, text_content

<<<<<<< HEAD
# def image_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         base64_image = base64.b64encode(img_file.read()).decode('utf-8')
#     return base64_image
=======
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')
    return base64_image
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d

async def take_screenshot(page, screenshot_path):
    await page.screenshot(path=screenshot_path)

@app.post("/scrape/")
async def scrape(url_item: URLItem):
    url = url_item.url
<<<<<<< HEAD
    screenshot_path = 'screenshot-' + str(time.time()) +'.png'
=======
    screenshot_path = 'screenshot.png'
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        # Wait until the page is fully loaded
        await page.wait_for_selector('body')
        
        # Extract HTML content and text without HTML tags
        html_content = await page.content()
        html_content, text_content = extract_content(html_content)
        
        # Take a screenshot of the webpage
        await take_screenshot(page, screenshot_path)
<<<<<<< HEAD
        
        await browser.close()
    screenshot_url = f"/static/{screenshot_path}"
    print(screenshot_url)
=======
        base64Image = image_to_base64(screenshot_path)
        
        await browser.close()
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d
    
    return {
        "html_content": html_content,
        "text_content": text_content,
<<<<<<< HEAD
        "downloadable_screenshot_path": screenshot_url
=======
        "screenshot_path": base64Image
>>>>>>> eeeeb8dcfad0f298925571b822cc0cc22202729d
    }
