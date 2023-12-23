from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
def Home():
    return "Welcome"

@app.get('/name/{Name}')
def Name(Name):
    return Name

if __name__ == "__main__":
    uvicorn.run("app:app",reload = True)