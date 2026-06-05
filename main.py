from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "nombre": "Jaqueline Gabriela Calanche Rodiguez",
        "album_favorito": "Fallen"
    }