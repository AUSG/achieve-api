from typing import Any, List

import schemas
from fastapi import APIRouter

from schemas.request import PostCreateRequest

router = APIRouter()


@router.post("/", response_model=List[schemas.Message])
def create_post(post: PostCreateRequest) -> Any:
    """
    create post
    :return:
    """
    new_post = Message(
        
    )
    # TODO
    # Create Model Instance
    item = schemas.Item(title="sample item", description="sample_description")
    return [item]
