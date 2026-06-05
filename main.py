from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "nombre": "Jaqueline Gabriela Calanche Rodiguez",
        "cancion_favorita": "evanescence bring me to life"
    }