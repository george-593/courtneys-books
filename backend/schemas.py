from pydantic import BaseModel
from typing import Optional


class BlogPostCreate(BaseModel):
    title: str
    content: str


class BlogPostPatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class BlogPostOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
