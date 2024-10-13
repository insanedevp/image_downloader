# tests/test_app.py
import pytest
from httpx import AsyncClient
from app import app
import os


@pytest.mark.asyncio
async def test_download_images():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/download-images/", json={
            "query": "test",
            "max_images": 2,
            "resize_width": 100,
            "resize_height": 100
        })
        assert response.status_code == 200
        assert response.json()["message"] == "Images downloaded and stored successfully."
