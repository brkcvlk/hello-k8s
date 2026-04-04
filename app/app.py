from fastapi import FastAPI, Response, status
from contextlib import asynccontextmanager
from datetime import datetime, UTC

startup_time = None

@asynccontextmanager
async def lifespan(app : FastAPI):
    global startup_time
    startup_time = datetime.now(UTC)
    yield

app = FastAPI(title="hello-k8s", lifespan=lifespan)

# livenessProbe
@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now(UTC)}

# readinessProbe
@app.get("/ready")
def ready(response: Response):
    if startup_time is None:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not ready"}
    return {"status": "ready", "since": startup_time}


@app.get("/")
def root():
    return {"message": "hello k8s!"}
