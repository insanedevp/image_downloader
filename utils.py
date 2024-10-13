
# utils.py
import os
import aiohttp
import asyncio
from PIL import Image
from io import BytesIO
from database import SessionLocal
from models import ImageModel
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError
from aiohttp import ClientSession, ClientTimeout
from typing import Optional, Tuple

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

async def fetch_image_urls(query: str, max_images: int) -> list:
    search_url = "https://www.googleapis.com/customsearch/v1"
    image_urls = []
    start_index = 1  # Start from the first result

    async with ClientSession(timeout=ClientTimeout(total=60)) as session:
        while len(image_urls) < max_images and start_index <= 91:
            params = {
                "q": query,
                "cx": GOOGLE_CSE_ID,
                "key": GOOGLE_API_KEY,
                "searchType": "image",
                "num": 10,
                "start": start_index
            }
            async with session.get(search_url, params=params) as response:
                if response.status != 200:
                    print(f"Error fetching results: {response.status}")
                    break
                data = await response.json()
                items = data.get("items")
                if not items:
                    print("No more items found.")
                    break
                for item in items:
                    link = item.get("link")
                    if link and link not in image_urls:
                        image_urls.append(link)
                        if len(image_urls) >= max_images:
                            break
                start_index += 10  # Move to the next page
    return image_urls

async def download_and_resize_image(session: ClientSession, url: str, width: int, height: int) -> Optional[Tuple[bytes, str]]:
    try:
        async with session.get(url, timeout=ClientTimeout(total=30)) as response:
            if response.status != 200:
                print(f"Failed to download image {url}: {response.status}")
                return None
            image_data = await response.read()
            image = Image.open(BytesIO(image_data)).convert("RGB")
            image = image.resize((width, height))
            buffer = BytesIO()
            image.save(buffer, format='PNG')
            return buffer.getvalue(), url
    except Exception as e:
        print(f"Failed to download or process image {url}: {e}")
        return None

async def process_images(request):
    image_urls = await fetch_image_urls(request.query, request.max_images)
    tasks = []
    semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent tasks
    async with ClientSession() as session:
        for url in image_urls:
            tasks.append(download_and_resize_image_with_semaphore(session, url, request.resize_width, request.resize_height, semaphore))
        images = await asyncio.gather(*tasks)

    # Filter out any failed downloads
    images = [img for img in images if img is not None]

    if not images:
        raise Exception("No images were downloaded successfully.")

    # Save images to the database
    db = SessionLocal()
    try:
        for image_data, url in images:
            if not db.query(ImageModel).filter_by(url=url).first():
                image_record = ImageModel(url=url, data=image_data)
                db.add(image_record)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Database error: {e}")
        raise e
    finally:
        db.close()

async def download_and_resize_image_with_semaphore(session, url, width, height, semaphore):
    async with semaphore:
        return await download_and_resize_image(session, url, width, height)
