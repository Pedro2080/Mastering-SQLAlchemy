from sqlalchemy import Column, ForeignKey, Table
from models.model_base import ModelBase
from models.ice_pop_type import IcePopType


# invoices has many lotes

invoices_lotes = Table(
    "invoices_lotes",
    ModelBase.metadata,
    Column("invoices_id", ForeignKey("invoices.id")),
    Column("lote_id", ForeignKey("lotes.id")),
)

# ice poo has many ingredients
ice_pop_ingredients = Table(
    "ice_pop_ingredients",
    ModelBase.metadata,
    Column("ice_pop_id", ForeignKey("ice_pops.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
)

# ice pop has many preservatives
ice_pop_preservatives = Table(
    "ice_pop_preservatives ",
    ModelBase.metadata,
    Column("ice_pop_id", ForeignKey("ice_pops.id")),
    Column("preservative_id", ForeignKey("preservatives.id")),
)

# ice po has many nutritional additives
ice_pop_nutritional_additives = Table(
    "ice_pop_nutritional_additives ",
    ModelBase.metadata,
    Column("ice_pop_id", ForeignKey("ice_pops.id")),
    Column("nutritional_additives_id", ForeignKey("nutritional_additives.id")),
)
