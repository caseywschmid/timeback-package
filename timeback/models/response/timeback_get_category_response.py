"""Response model for getting a category.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

Per spec: HTTP 200 with category object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_category import TimebackCategory


class TimebackGetCategoryResponse(BaseModel):
    """Response model for getting a single category.

    Attributes:
        - category (TimebackCategory): The requested category. See TimebackCategory for structure.
    """

    category: TimebackCategory = Field(..., description="The requested category")

