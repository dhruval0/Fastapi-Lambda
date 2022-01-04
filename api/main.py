from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def orchtel_home():
    return {"Welcome to": "lambda function"}

handler = Mangum(app = app)