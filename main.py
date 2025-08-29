from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI app!"}


@app.get("/info")
async def info():
    return {"server": "EC2", "phase": "2"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
