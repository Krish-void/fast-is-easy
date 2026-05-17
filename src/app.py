from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"fastapi": "i will damn crack it in 1 month as challenge"}
@app.get("/hello")
def hello_world():    
    return {"msg": "hello_world"}     # Json -> 
