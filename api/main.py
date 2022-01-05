from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def fastapi_home():
    return {"Welcome to": "lambda function"}

@app.get("/dhruval")
def dhruval_home():
    return {"Welcome to": "dhruval's lambda function"}

handler = Mangum(app = app)
