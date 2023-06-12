from fastapi import APIRouter 
#Devolver respuesta en formato json
from fastapi.responses import JSONResponse 

from fastapi import APIRouter

from utils.jwt_manager import create_token

from schemas.auth import User

auth_router = APIRouter()



@auth_router.post("/login", tags=["Auth"])
def login(User: User):
     if (User.email=="drogstore@gmail.com" and User.password =="@auth@1988@"):
         token: str = create_token(User.dict())
         return JSONResponse(content=token)
