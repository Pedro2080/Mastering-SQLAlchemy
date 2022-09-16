from typing import List, Optional

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from models.association_table import ice_pop_ingredients, ice_pop_preservatives, ice_pop_nutritional_additives
from models.model_base import ModelBase
from models.Ingredient import Ingredient
from models.preservative import Preservative
from models.nutritional_additives import NutritionalAdditives


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

    # One ice pop has many ingredients (has a list of ingredients)
    ingredients: List[Ingredient] = relationship("Ingredient", secondary=ice_pop_ingredients,
                                                  backref="ingredient", lazy="joined")

    # One ice pop has many preservatives or none
    preservatives: Optional[List[Preservative]] = relationship("Preservative", secondary=ice_pop_preservatives,
                                                               backref="preservative", lazy="joined")

    # One ice pop has many nutritional additives or none
    nutritional_additives: Optional[List[NutritionalAdditives]] = relationship("NutritionalAdditives",
                                                                               secondary=ice_pop_nutritional_additives,
                                                                               backref="nutritional_additive",
                                                                               lazy="joined")

    def __repr__(self) -> str:
        return f'<Ice Pop: {self.ice_pop_type.name} with teste {self.teste.name} and price {self.price}>'
