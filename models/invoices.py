from typing import List

from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from models.model_base import ModelBase
from models.lote import Lote
from association_table import invoices_lotes


class Invoice(ModelBase):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    value = Column(Integer, nullable=False)
    serial_number = Column(String(length=100), nullable=False)
    description = Column(String(length=200), nullable=False)

    seller_id = Column(Integer, ForeignKey("sellers.id"))
    seller = relationship("Seller", lazy="joined")

    # One invoice has many lotes and a lote has one invoice

    lotes: List[Lote] = relationship("Lote", secondary=invoices_lotes, backref="lote", lazy="dynamic")

    def __repr__(self) -> str:
        return f'<Invoice: {self.serial_number}>'
