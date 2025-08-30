import logging
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    logger.info("Accessing root endpoint")
    return {"message": "Welcome to my DevOps API!"}


@app.get("/info")
async def info():
    logger.info("Accessing info endpoint")
    return {"server": "AWS EC2", "app": "FastAPI", "version": "1.0"}


@app.get("/health")
async def health():
    logger.info("Accessing health endpoint")
    return {"status": "healthy"}
