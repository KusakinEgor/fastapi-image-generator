import uvicorn
from fastapi import FastAPI
from app.routes import auth
from app.routes import generate
from app.routes import images

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(generate.router, tags=["Generate"])
app.include_router(images.router, tags=["Images"])

@app.get("/")
async def root():
    return {"message": "Hello, AI Image Generator!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
