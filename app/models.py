from sqlalchemy import Integer, String, DateTime, Enum, Interval
from datetime import datetime, timedelta
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
import enum


class VideoStatus(str, enum.Enum):
    new = 'new'
    transcoded = 'transcoded'
    recognized = 'recognized'


class Video(Base):
    __tablename__ = 'videos'

    id: Mapped[int] = mapped_column(primary_key=True)
    video_path: Mapped[str] = mapped_column(String, nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    duration: Mapped[timedelta] = mapped_column(Interval, nullable=False)
    camera_number: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[VideoStatus] = mapped_column(Enum(VideoStatus), default=VideoStatus.new)
    created_at: Mapped[datetime] = mapped_column(DateTime)

