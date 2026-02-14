from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/") #функция обрабатывает только get запросы
async def root():
    return FileResponse("ind.html")

