from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.sql import func
from models.model_base import ModelBase


class Preservative(ModelBase):
    __tablename__ = "preservatives"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(length=45), unique=True, nullable=False)
    description = Column(String(length=45), nullable=False)

    def __repr__(self) -> str:
        return f'<Preservative: {self.name}>'
