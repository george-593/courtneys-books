from fastapi import APIRouter, Depends, HTTPException, status
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


@router.put("/{post_id}", response_model=schemas.BlogPostOut)
async def put_blog_post(
    post_id: int,
    post: schemas.BlogPostCreate,
    db: AsyncSession = Depends(dependencies.get_db),
):
    result = await db.execute(
        select(models.BlogPost).where(models.BlogPost.id == post_id)
    )
    existing_post = result.scalar_one_or_none()

    if existing_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")

    existing_post.title = post.title
    existing_post.content = post.content
    db.add(existing_post)
    await db.commit()
    await db.refresh(existing_post)
    return existing_post


@router.patch("/{post_id}", response_model=schemas.BlogPostOut)
async def patch_blog_post(
    post_id: int,
    post: schemas.BlogPostPatch,
    db: AsyncSession = Depends(dependencies.get_db),
):
    result = await db.execute(
        select(models.BlogPost).where(models.BlogPost.id == post_id)
    )
    existing_post = result.scalar_one_or_none()

    if existing_post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")

    if post.title != existing_post.title and post.title is not None:
        existing_post.title = post.title
    if post.content != existing_post.content and post.content is not None:
        existing_post.content = post.content
    db.add(existing_post)
    await db.commit()
    await db.refresh(existing_post)
    return existing_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_post(
    post_id: int, db: AsyncSession = Depends(dependencies.get_db)
):
    result = await db.execute(
        select(models.BlogPost).where(models.BlogPost.id == post_id),
    )
    post = result.scalar_one_or_none()
    if post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")

    await db.delete(post)
    await db.commit()
