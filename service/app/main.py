from fastapi import FastAPI
from pydantic import BaseModel
import time
from .model import predict
from .db import log_to_db
from prometheus_client import Counter, generate_latest

REQUEST_COUNT = Counter("requests_total", "Total requests")

app = FastAPI()

class Request(BaseModel):
    x: float

@app.get("/metrics")
def metrics():
    return generate_latest()

@app.post("/api/v1/predict")
def predict_api(req: Request):
    REQUEST_COUNT.inc()
    start = time.time()
    result = predict(req.x)
    latency = time.time() - start
    log_to_db(req.x, result, latency)
    return {"result": result}