from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from typing import Optional
from .models import VideoStatus

class VideoBase(BaseModel):
    id: int
    video_path: str
    start_time: datetime
    duration: timedelta
    camera_number: int
    location: str
    status: VideoStatus
    created_at: datetime

class PostVideoBase(BaseModel):
    video_path: str = Field(..., min_length=1)
    start_time: datetime = Field(..., lt=datetime.now())
    duration: timedelta = Field(..., gt=timedelta(0))
    camera_number: int = Field(..., gt=0)
    location: str = Field(..., min_length=1)


class StatusBase(BaseModel):
    status: VideoStatus


class FiltersBase(BaseModel):
    status: Optional[list[VideoStatus]] = None
    camera_number: Optional[list[int]] = None
    location: Optional[list[str]] = None
    start_time_from: Optional[datetime] = None
    start_time_to: Optional[datetime] = None