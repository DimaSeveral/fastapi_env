from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.get("/")
async def root():
    return FileResponse("ind.html")

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}


#uvicorn main:app --reload
#http://127.0.0.1:8000

#curl.exe -X POST "http://127.0.0.1:8000/calculate" -H "Content-Type: application/json" -d '{\"num1\":5,\"num2\":10}'