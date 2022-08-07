from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# String de conexão Windows Server.
parametros = os.getenv("SQL_CONNECTION")

# Convertendo a string para um padrão de URI HTML.
url_db = quote_plus(parametros)

# Conexão.
# Para debug utilizar echo=True
engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db, echo=True)

# Session é instanciado posteriormente para interação com a tabela.
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()