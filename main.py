from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
import listen_to_changes  # Asegúrate de que este archivo y función existen
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB = os.environ.get("MONGO_DB")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mongo_client = AsyncIOMotorClient(MONGO_URI)
    task = asyncio.create_task(listen_to_changes.listen_to_changes(app.state.mongo_client ))
    yield
    task.cancel()
    app.state.mongo_client.close()
    try:
        await task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "API corriendo y escuchando cambios en MongoDB"}