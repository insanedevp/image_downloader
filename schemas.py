# schemas.py

from pydantic import BaseModel, Field


class ImageRequest(BaseModel):
    query: str = Field(..., example="cute kittens")
    max_images: int = Field(..., gt=0, le=100, example=5)
    resize_width: int = Field(800, gt=0, example=800)
    resize_height: int = Field(600, gt=0, example=600)
