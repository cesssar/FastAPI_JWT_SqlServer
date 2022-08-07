'''
https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a

'''

import uvicorn  

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)