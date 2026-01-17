from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from datetime import datetime
from .models import Video, VideoStatus
from .schemas import PostVideo, GetVideo, Status

async def create_video(db: AsyncSession, video: PostVideo) -> Video:
    db_video = Video(
        video_path=video.video_path,
        start_time=video.start_time,
        duration=video.duration,
        camera_number=video.camera_number,
        location=video.location
    )
    db.add(db_video)
    await db.commit
    await db.refresh(db_video)
    return db_video


async def get_all_videos(db: AsyncSession,
            status: list[VideoStatus] | None = None,
            camera_number: list[int] | None = None,
            location: list[str] | None = None,
            start_time_from: datetime | None = None,
            start_time_to: datetime | None = None):
    query = select(Video)
    if status:
        query = query.where(Video.status == status)
    if camera_number:
        query = query.where(Video.camera_number == camera_number)
    if location:
        query = query.where(Video.location == location)
    if start_time_from:
        query = query.where(Video.start_time > start_time_from)
    if start_time_to:
        query = query.where(Video.start_time < start_time_to)
    
    videos = await db.execute(query)
    return videos.scalars().all()


async def get_video(db: AsyncSession, id: GetVideo) -> Video:
    query = select(Video).where(Video.id == id)
    result = await db.execute(query)
    video = result.scalars().one()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Нет видео с ID: {id}")
    return video


async def update_video(db: AsyncSession, id: GetVideo, status: Status) -> Video | None:
    video = await get_video(db, id)
    video.status = status
    await db.commit()
    await db.refresh(video)
    return video
