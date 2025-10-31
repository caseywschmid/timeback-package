"""Response model for creating a OneRoster User.

Represents the body returned by:
- POST /ims/oneroster/rostering/v1p2/users/
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_user import TimebackUser


class TimebackCreateUserResponse(BaseModel):
    user: TimebackUser = Field(..., description="Created user object")


