from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def orchtel_home():
    return {"Welcome to": "lambda function"}