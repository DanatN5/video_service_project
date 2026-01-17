from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from .models import VideoStatus

class Video(BaseModel):
    id: int
    video_path: str
    start_time: datetime
    duration: timedelta
    camera_number: int
    location: str
    status: VideoStatus
    created_at: datetime

class PostVideo(BaseModel):
    video_path: str = Field(..., min_length=1)
    start_time: datetime = Field(..., lt=datetime.now())
    duration: timedelta = Field(..., gt=timedelta(0))
    camera_number: int = Field(..., gt=0)
    location: str = Field(..., min_length=1)


class Status(BaseModel):
    status: VideoStatus

