from fastapi import FastAPI

app = FastAPI(title="fastapi-app")


@app.get("/")
def read_root():
    return {"mensagem": "API no ar"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/soma/{a}/{b}")
def soma(a: int, b: int):
    return {"resultado": a + b}
