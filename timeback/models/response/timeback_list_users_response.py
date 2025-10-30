from typing import List
from pydantic import BaseModel, Field
from timeback.models.timeback_user import TimebackUser


class TimebackListUsersResponse(BaseModel):
    """Response model for paginated users list.

    Mirrors OneRoster list response envelope for users as documented in
    `timeback/docs/oneroster/rostering/list_users.md`.
    """

    users: List[TimebackUser] = Field(..., description="List of users")
    totalCount: int = Field(..., description="Total number of results")
    pageCount: int = Field(..., description="Total number of pages")
    pageNumber: int = Field(..., description="Current page number")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")
