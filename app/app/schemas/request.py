from datetime import datetime

from pydantic import BaseModel


class RequestBase(BaseModel):
    pass

class PostRequest(RequestBase):
    type: str
    channel: str
    user: str
    text: str
    ts: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }

class PostCreateRequest(PostRequest):
    pass

class PostUpdateRequest(PostRequest):
    edit_user: str
    edit_ts: datetime



