from models.medicamentos import Medicamentos as MedicamentoModel
from schemas.drogstore import Farmacia


class DrogstoreService():
    def __init__(self, db) -> None:
        self.db = db

    def get_drogstore(self):
        resutl = self.db.query(MedicamentoModel).all()
        return resutl
    
    def get_drogstore_id(self, id: int):
        result = self.db.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
        return result
    
    def get_drogstore_tipo(self, tipo):
        result = self.db.query(MedicamentoModel).filter(MedicamentoModel.tipo == tipo).first()
        return result
    
    def put_drogstore_tipo(self, farmacia: Farmacia):
        new_med = MedicamentoModel(**farmacia.dict())
        self.db.add(new_med)
        self.db.commit()
        return
    
    def update_drogstore_id(self, id: int, farmacia: Farmacia):
        up_med = self.db.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
 
        up_med.nombre = farmacia.nombre
        up_med.precio = farmacia.precio
        up_med.descripcion = farmacia.descripcion
        up_med.tipo = farmacia.tipo        
        self.db.commit()
        return 
    
    def delete_drogstore_id(self, id: int):
        del_med = self.db.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
        self.db.delete(del_med)
        self.db.commit()
        
        return