import logging
import os
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Custom metric
custom_requests = Counter(
    "custom_requests_total", "Total custom requests", ["endpoint"]
)


@app.get("/")
async def root():
    logger.info("Accessing root endpoint")
    custom_requests.labels(endpoint="root").inc()
    return {"message": "Welcome to my DevOps API!"}


@app.get("/info")
async def info():
    logger.info("Accessing info endpoint")
    custom_requests.labels(endpoint="info").inc()
    return {"server": "AWS EC2", "app": "FastAPI", "version": "1.0"}


@app.get("/health")
async def health():
    logger.info("Accessing health endpoint")
    custom_requests.labels(endpoint="health").inc()
    env = os.getenv("APP_ENV", "unknown")
    if env != "production":
        raise HTTPException(status_code=503, detail="Not in production mode")
    return {"status": "healthy", "env": env}
