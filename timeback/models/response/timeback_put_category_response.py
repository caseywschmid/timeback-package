"""Response model for updating/creating a category.

Represents the body returned by:
- PUT /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

Per spec: HTTP 201 with category object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_category import TimebackCategory


class TimebackPutCategoryResponse(BaseModel):
    """Response model for PUT category.

    Attributes:
        - category (TimebackCategory): The updated/created category. See TimebackCategory for structure.
    """

    category: TimebackCategory = Field(..., description="The updated/created category")

