from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def greet_json():
    return {"Hello": "World!"}
