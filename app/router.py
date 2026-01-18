from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PostVideoBase, VideoBase, StatusBase, FiltersBase
from .database import AsyncSessionLocal
from .dependencies import get_video_filters
from . import cru

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/videos", response_model=VideoBase)
async def create_video(video: PostVideoBase, db: AsyncSession = Depends(get_db)):
    return await cru.create_video(db, video)

@router.get("/videos", response_model=list[VideoBase])
async def get_all_videos(db: AsyncSession = Depends(get_db), filters: FiltersBase = Depends(get_video_filters)):
    return await cru.get_all_videos(db,  filters)

@router.get("/videos/{video_id}", response_model=VideoBase)
async def get_video(video_id: int, db: AsyncSession = Depends(get_db)):
    return await cru.get_video(db, video_id)

@router.patch("/videos/{video_id}/status", response_model=VideoBase)
async def update_video(video_id: int, status: StatusBase, db: AsyncSession = Depends(get_db)):
    return await cru.update_video(db, video_id, status.status)

