from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def index():
    try:
        return JSONResponse(status_code=200, content={
            "message": "Hello Planet"
        })
    except ValueError as e:
        return JSONResponse(status_code=500, content={
            "message": "Ocorreu um erro interno: {}".format(e)
        })