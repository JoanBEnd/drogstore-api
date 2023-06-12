from fastapi import APIRouter
from fastapi import  Body, Query, Depends

#Devolver respuesta en formato json
from fastapi.responses import JSONResponse 


#devolvera una lista y esta lo definimos en la funcion de esta form (-> List[])
from typing import List

from config.database import session
from models.medicamentos import Medicamentos as MedicamentoModel
from fastapi.encoders import jsonable_encoder
from middelwares.jwt_mideware import JWTBearer

from services.drogstore import DrogstoreService

from schemas.drogstore import Farmacia
drogstore_router = APIRouter()




@drogstore_router.get("/obtener_listado", tags=["Funciones"], response_model=List[Farmacia], dependencies=[Depends(JWTBearer())] )
def get_Farmacia() -> List[Farmacia]:
    db =session()
    listado_ = DrogstoreService(db).get_drogstore()
    return jsonable_encoder(listado_)


@drogstore_router.get("/obtener_medicamento_by_id/{id}", tags=["Funciones"], response_model=Farmacia)
def get_medicamento(id: int) ->  Farmacia : 
    db = session()
    result = DrogstoreService(db).get_drogstore_id(id)
    if not result:
         return JSONResponse(content={"message": "No se encontró la información"})
    return JSONResponse(content=jsonable_encoder(result))

    #medicamento = list(filter(lambda item: item["id"] == id, list_farmacia))
    #como estoy obteniendo la lista con todo y [],voy a sacar el resultado 
    #medicamento = medicamento[0]
    #return JSONResponse(content=medicamento)

@drogstore_router.post("/registrar_medicamento_basemodel", tags=["Funciones"], response_model= dict)
def registrar_medicamento_BaseModel(farmacia: Farmacia) -> dict:
    
    db = session()
    DrogstoreService(db).put_drogstore_tipo(farmacia)

    return JSONResponse(content={"message": "Se registró el medicamento"})


@drogstore_router.put("/modificar_medicamento_basemodel/{id}", tags=["Funciones"], response_model=dict)
def put_medicamento_basemodel(id: int , farmacia: Farmacia) -> dict:
    print("holaaaa")
    db = session() 
    result_ = DrogstoreService(db).get_drogstore_id(id)
    if not result_ :
           return JSONResponse(content={"message": "No se encontró la información"})    
    DrogstoreService(db).update_drogstore_id(id, farmacia)





@drogstore_router.delete("/eliminar_medicamento/{id}", tags=["Funciones"], response_model=dict)
def delete_medicamento(id: int) -> dict:
    
    db = session()
    resultado = DrogstoreService(db).get_drogstore_id(id)
    
    if not resultado:
         return JSONResponse(content={"message": "No se encontró la información"})
    
    DrogstoreService(db).delete_drogstore_id(id)
    return JSONResponse(content={"message": "Se eliminó el medicamento"})
 
     

#TIPO QUERY
@drogstore_router.get("/obtener_medicamento_by_tipo/", tags=["Funciones Query"], response_model= List[Farmacia])
def Get_medicamento_tipo_by_tipo(tipo: str = Query(min_length=5, max_length=15)) -> List[Farmacia]:
      bd = session()
      new_dato = DrogstoreService(bd).get_drogstore_tipo(tipo)
      if not new_dato:
           return JSONResponse(content={"mesagge":"No se encontró información."})
      return JSONResponse(content=jsonable_encoder(new_dato))
      #data = list(filter(lambda item: item["tipo"] == tipo, list_farmacia))
      #return JSONResponse(content=data)
