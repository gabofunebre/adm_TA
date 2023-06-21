from datetime import date
from sqlalchemy import create_engine, Column, Date, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer


Base = declarative_base()
engine = create_engine('sqlite:///controlDinero.db')
Session = sessionmaker(bind=engine)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Registro(Base):
    __tablename__ = 'registros'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    descripcion = Column(String)
    monto = Column(Float)
    inOut = Column(String)
    origen = Column(String)
    nota = Column(String)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship(Usuario)

    def __init__(self, fecha, descripcion, monto, inOut, origen, nota, usuario):
        self.fecha = fecha
        self.descripcion = descripcion
        self.monto = monto
        self.inOut = inOut
        self.origen = origen
        self.nota = nota
        self.usuario = usuario

def validar_credenciales(username, password):
    session = Session()
    usuario = session.query(Usuario).filter_by(username=username, password=password).first()
    session.close()

    if usuario:
        return usuario.username, usuario.id
    else:
        return None, None

def obtener_registros_entre_fechas(fecha_inicio, fecha_fin):
    session = Session()
    registros = session.query(Registro).filter(Registro.fecha.between(fecha_inicio, fecha_fin)).all()
    session.close()
    return registros

def crear_registro(fecha, descripcion, monto, inOut, origen, nota, id_usuario):
    session = Session()
    usuario = session.query(Usuario).get(id_usuario)
    session.close()
    registro = Registro(fecha, descripcion, monto, inOut, origen, nota, usuario)
    return registro

def agregar_usuario(username, password):
    usuario = Usuario(username=username, password=password)
    session = Session()
    session.add(usuario)
    session.commit()
    session.close()

def insertar_registro(registro):
    session = Session()
    session.add(registro)
    session.commit()
    session.close()

def eliminar_registro(id_registro):
    session = Session()
    registro = session.query(Registro).get(id_registro)
    if registro:
        session.delete(registro)
        session.commit()
    session.close()
