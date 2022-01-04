from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def orchtel_home():
    return {"Welcome to": "lambda function"}

@app.get("/ab")
def ab_home():
    return {"Welcome to": "AB's lambda function"}

handler = Mangum(app = app)
