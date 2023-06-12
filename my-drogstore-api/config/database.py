import os
from sqlalchemy import create_engine # para el motor de la base de datos
from sqlalchemy.orm.session import sessionmaker #sesion para conectar a la base
from sqlalchemy.ext.declarative import declarative_base #manipular las tablas

# nombre de la base
sqlite_database = "../database.sqlite" 

#en la variable se guarda el directorio de este archivo
base_dir = os.path.dirname(os.path.realpath(__file__)) 

 # la forma de conectarse a una base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_database)}"

#representa el motor de la base de datos
engine = create_engine(database_url, echo=True)

#para conectar a la base de datos 
#bind: enlaza al motor de la base de datos
session = sessionmaker(bind=engine)

base = declarative_base()