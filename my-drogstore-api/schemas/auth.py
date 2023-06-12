
#forma de envio de parametros
from pydantic import BaseModel  

class User(BaseModel):
     email: str
     password: str