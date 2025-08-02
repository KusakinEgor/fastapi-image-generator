import uvicorn
from fastapi import FastAPI
from app.routes import auth, generate, images, history, tags
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.utils.rate_limiter import limiter

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

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
