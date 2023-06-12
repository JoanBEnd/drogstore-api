from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
 
from config.database import  engine, base  
from middelwares.error_handler import ErrorHandler
from routers.drogstore import drogstore_router
from routers.auth import auth_router

app = FastAPI()
app.title ="Api de Farmacia"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(auth_router)
app.include_router(drogstore_router)

base.metadata.create_all(bind=engine) 


@app.get("/saludo", tags=["Saludos"])
def Saludar():
    return "Saludos a todos" 

@app.get("/pagina", tags=["Saludos"])
def pagina():
    return HTMLResponse("<h1> Farmacia Global </h1>")
