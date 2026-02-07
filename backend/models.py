from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class BlogPost(Base):
    __tablename__ = "blogposts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
