from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import PostVideo, Video, GetVideo, Status
from .database import AsyncSessionLocal
from . import cru

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/videos", response_model=Video)
async def create_video(video: PostVideo, db: AsyncSession = Depends(get_db)):
    return await cru.create_video(db, video)

@router.get("/videos", response_model=list[Video])
async def get_all_videos(db: AsyncSession = Depends(get_db)):
    return await cru.get_all_videos(db)

@router.get("/videos/{video_id}", response_model=Video)
async def get_video(video_id: GetVideo, db: AsyncSession = Depends(get_db)):
    return await cru.get_video(db, video_id)

@router.patch("/videos/{video_id}/status", response_model=Video)
async def update_video(video_id: GetVideo, status: Status, db: AsyncSession = Depends(get_db)):
    return await cru.update_video(db, video_id, status)

