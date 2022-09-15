from sqlalchemy import Column, ForeignKey, Table
from models.model_base import ModelBase

# invoices has many lotes

invoices_lotes = Table(
    "invoices_lotes",
    ModelBase.metadata,
    Column("invoices_id", ForeignKey("invoices.id")),
    Column("lote_id", ForeignKey("lotes.id")),
)