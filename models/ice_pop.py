from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func
from models.model_base import ModelBase


class IcePop(ModelBase):
    __tablename__ = "ice_pops"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    price = Column(Integer, nullable=False)

    teste_id = Column(Integer, ForeignKey("testes.id"))
    teste = relationship("Teste", lazy="joined")

    packing_type_id = Column(Integer, ForeignKey("packing_types.id"))
    packing_type = relationship("PackingType", lazy="joined")

    ice_pop_type_id = Column(Integer, ForeignKey("ice_pops_types.id"))
    ice_pop_type = relationship("IcePopType", lazy="joined")

    def __repr__(self) -> str:
        return f'<Ice Pop: {self.type_ice_pop.name} with teste {self.teste.name} price {self.pr}>'
