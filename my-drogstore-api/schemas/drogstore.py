

#forma de envio de parametros
from pydantic import BaseModel
from typing import Optional

# Para validar campos
from pydantic import  Field 

class Farmacia(BaseModel):
     id: Optional[int] = None
     nombre: str = Field( max_length=15)
     precio: float 
     descripcion: str = Field( max_length=50)
     tipo: str = Field( max_length=50)

     class Config:
          schema_extra = {
               "example" : {
                    "id": 1,
                    "nombre": "panadol",
                    "precio": 2,
                    "descripcion": "para el dolor",
                    "tipo": "aines", 
               }
          }