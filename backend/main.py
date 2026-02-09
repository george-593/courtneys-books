from fastapi import FastAPI
from backend.routes import blog_posts

app = FastAPI()

app.include_router(blog_posts.router, prefix="/blog-posts", tags=["Blog Posts"])


@app.get("/")
def get_root():
    return {"status": "API Online"}
