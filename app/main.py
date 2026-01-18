from fastapi import FastAPI
from .router import router
from .database import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello world!'}