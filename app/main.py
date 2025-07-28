import uvicorn
from fastapi import FastAPI
from app.routes import auth, generate, images, history, tags

app = FastAPI()

app.include_router(auth.router, tags=["🔐Auth"])
app.include_router(generate.router, tags=["🛠️Generate"])
app.include_router(images.router, tags=["🖼️Images"])
app.include_router(history.router, tags=["📜History"])
app.include_router(tags.router, tags=["📌Tags"])

@app.get("/", tags=["🌳Root"])
async def root():
    return {"message": "Hello, AI Image Generator!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
