from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from .models import Video
from .schemas import PostVideo, GetVideo

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


async def get_all_videos(db: AsyncSession):
    return db.query(Video).all()


async def get_video(db: AsyncSession, id: GetVideo) -> Video:
    video = db.query(Video).filter(Video.id == id).first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Нет видео с ID: {id}")
    return video