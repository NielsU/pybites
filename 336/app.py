from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    msg = "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
    return {"message": msg}
