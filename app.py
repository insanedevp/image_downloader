# app.py
from fastapi import FastAPI, HTTPException
from schemas import ImageRequest
from utils import process_images

app = FastAPI()


@app.post("/download-images/")
async def download_images(request: ImageRequest):
    try:
        await process_images(request)
        return {"message": "Images downloaded and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
