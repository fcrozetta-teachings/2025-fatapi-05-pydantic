from fastapi import FastAPI

app = FastAPI(title="My fist API")


@app.get("/")
def read_root():
    return {"Hello": "World"}
