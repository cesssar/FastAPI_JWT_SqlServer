from fastapi import FastAPI, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from app import models, schemas
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer
from app.database import *

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI - JWT Authentication",
    description="Exemplo de API com autenticação JWT e conexão com banco de dados SQL Server. 🚀",
    version="1.0.0",
    contact={
        "name": "Cesar Steinmeier",
        "email": "cesssar@me.com"
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependencia
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.post("/login", tags=["Login"])
def login(db: Session = Depends(get_db), usuario: schemas.Usuario = Body(..., embed=True)):
    u = db.query(models.Usuario).filter(models.Usuario.usuario == usuario.usuario).first()
    if u is None or models.Usuario.check_senha(u, usuario.senha) is False:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return signJWT(u.usuario)

@app.get("/usuarios/", response_model=List[schemas.Usuario], dependencies=[Depends(JWTBearer())], tags=["Usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    registros = db.query(models.Usuario).all()
    return registros 

@app.get("/usuarios/{usuario}", response_model=schemas.Usuario, tags=["Usuarios"])
def listar_usuario(usuario: str, senha: str, db: Session = Depends(get_db)):
    registro = db.query(models.Usuario).filter(models.Usuario.usuario == usuario).first()
    if registro is None or registro.check_senha(senha) is False:
        raise HTTPException(status_code=404, detail="Usuario não encontrado ou senha incorreta")
    return registro

@app.post("/usuarios/", response_model=schemas.Usuario, tags=["Usuarios"])
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    db_usuario  = db.query(models.Usuario).filter(models.Usuario.usuario == usuario.usuario).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    db_usuario = models.Usuario(usuario=usuario.usuario)
    db_usuario.set_senha(usuario.senha)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario