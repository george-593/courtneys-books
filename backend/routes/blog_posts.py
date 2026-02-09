from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend import models, schemas, dependencies

router = APIRouter()


@router.post(
    "/", response_model=schemas.BlogPostOut, status_code=status.HTTP_201_CREATED
)
async def create_blog_post(
    post: schemas.BlogPostCreate, db: AsyncSession = Depends(dependencies.get_db)
):
    new_post = models.BlogPost(**post.model_dump())
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


@router.get("/", response_model=list[schemas.BlogPostOut])
async def get_blog_posts(db: AsyncSession = Depends(dependencies.get_db)):
    result = await db.execute(select(models.BlogPost))
    return result.scalars().all()


@router.get("/{post_id}", response_model=schemas.BlogPostOut)
async def get_blog_post(post_id: int, db: AsyncSession = Depends(dependencies.get_db)):
    result = await db.execute(
        select(models.BlogPost).where(models.BlogPost.id == post_id),
    )
    post = result.scalar_one_or_none()
    if post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return post
