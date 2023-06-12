from config.database import base
from sqlalchemy import Column, Integer, String, Float


class Medicamentos(base):

    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key= True)
    nombre = Column(String)
    precio = Column(Float)
    descripcion = Column(String)
    tipo = Column(String)