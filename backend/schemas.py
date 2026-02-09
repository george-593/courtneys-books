from pydantic import BaseModel


class BlogPostCreate(BaseModel):
    title: str
    content: str


class BlogPostOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
