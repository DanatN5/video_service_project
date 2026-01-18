from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from datetime import datetime
from .models import Video
from .schemas import PostVideoBase, StatusBase, FiltersBase

async def create_video(db: AsyncSession, video: PostVideoBase) -> Video:
    db_video = Video(
        video_path=video.video_path,
        start_time=video.start_time,
        duration=video.duration,
        camera_number=video.camera_number,
        location=video.location,
        created_at=datetime.now()
    )
    db.add(db_video)
    await db.commit()
    await db.refresh(db_video)
    return db_video


async def get_all_videos(db: AsyncSession, filters: FiltersBase):
    query = select(Video)
    if filters.status:
        query = query.where(Video.status.in_(filters.status))
    if filters.camera_number:
        query = query.where(Video.camera_number.in_(filters.camera_number))
    if filters.location:
        query = query.where(Video.location.in_(filters.location))
    if filters.start_time_from:
        query = query.where(Video.start_time > filters.start_time_from)
    if filters.start_time_to:
        query = query.where(Video.start_time < filters.start_time_to)
    
    videos = await db.execute(query)
    return videos.scalars().all()


async def get_video(db: AsyncSession, id: int) -> Video:
    try:
        query = select(Video).where(Video.id == id)
        result = await db.execute(query)
        video = result.scalars().one()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Нет видео с ID: {id}")
    return video


async def update_video(db: AsyncSession, id: int, status: StatusBase) -> Video | None:
    video = await get_video(db, id)
    video.status = status
    await db.commit()
    await db.refresh(video)
    return video
