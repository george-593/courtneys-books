from pydantic import BaseModel
from datetime import datetime
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
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
