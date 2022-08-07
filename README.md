# FastAPI com JWT e conexão com banco de dados SQL Server 🚀

**Esquema básico de API em Python com FastAPI e autenticação JWT**

## Requisitos

- Python 3.6+
- FastAPI
- PyJWT
- SQLAlchemi

Recomenda-se criar um ambiente isolado para instalar as dependências (<a href="https://docs.python.org/3/library/venv.html">venv</a>)

```console
$ pip install -r requirements.txt

```

Criar um arquivo .env na pasta app com a string de conexão ao banco de dados SQL Server

SQL_CONNECTION = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;PORT=1433;DATABASE=JD_SPB;UID=sa;PWD=minha_senha'

## Executar

```console
$ python main.py
```

Créditos: <a href="https://testdriven.io/blog/fastapi-jwt-auth/">Abdulazeez Abdulazeez Adeshina</a> e <a href="https://blog.logrocket.com/server-side-rendering-with-fastapi-and-mysql/">Ekekenta Odionyenfe</a>
