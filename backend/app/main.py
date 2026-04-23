from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def route():
    return {"messg":"backend"}

@app.get("/test_db")
def route():
    return {"messg":"db"}

@app.get("/test_db1")
def route():
    return {"messg":"db1"}