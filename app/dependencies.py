from typing import List, Optional
from fastapi import Query
from .schemas import FiltersBase
from .models import VideoStatus

def get_video_filters(status: Optional[list[VideoStatus]] = Query(default=None),
                      camera_number: Optional[list[int]] = Query(None),
                      location: Optional[list[str]] = Query(None)):
    return FiltersBase(
        status=status,
        camera_number=camera_number,
        location=location
    )
