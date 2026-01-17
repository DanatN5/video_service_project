from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from .database import AsyncSessionLocal
from . import cru, schemas

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/videos", response_model=schemas.Video)
async def create_video(video: schemas.PostVideo, db: AsyncSession = Depends(get_db)):
    return await cru.create_video(db, video)

@router.post("/videos", response_model=list[schemas.Video])
async def get_all_videos(db: AsyncSession = Depends(get_db)):
    return await cru.get_all_videos(db)

