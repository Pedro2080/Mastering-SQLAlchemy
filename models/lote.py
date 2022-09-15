from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func
from models.model_base import ModelBase
from models.ice_pop_type import IcePopType


class Lote(ModelBase):
    __tablename__ = "lotes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    quantity = Column(Integer, nullable=False)

    ice_pop_id = Column(Integer, ForeignKey("ice_pops_types.id"))
    ice_pop = relationship("IcePopType", lazy="joined")

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'
