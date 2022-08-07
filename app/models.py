from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


from app.database import Base

class Usuario(Base):
    __tablename__ = 'USUARIO'

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(32), index=True, unique=True)
    senha = Column(String(255))

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)