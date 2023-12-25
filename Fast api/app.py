from fastapi import FastAPI, Path
import uvicorn
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()


class Students(BaseModel):
    name: str = Field(None, title="Name of the Student", max_length=10)
    age: int


@app.get("/")
def Home():
    return "Welcome"


@app.get("/name/{Name}")  # path parameter
def Name(Name):
    return Name


@app.get("/query")  # query parameter
def queryy(name: str, age: int):
    return {"name": name, "age": age}


@app.get("/pvalid/{name}/{age}")  # Path Validation
def pvalid(
    *,
    name: str = Path(..., min_length=3, max_length=10),
    age: int = Path(..., ge=1, le=30)
):
    return {"name": name, "age": age}


@app.post("/Pyd/")  # pydantic model
def pyd(s: Students):
    return s


@app.get("/Hello/")  # HTML
def Html():
    ret = """
    <html>
    <body>
    <h1> Welcome!</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=ret)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
