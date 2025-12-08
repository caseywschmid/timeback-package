"""Request model for updating/creating a category.

PUT /ims/oneroster/gradebook/v1p2/categories/{sourcedId}
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_category import TimebackCategory


class TimebackPutCategoryRequest(BaseModel):
    """Request model for PUT /categories/{sourcedId}.
    
    Attributes:
        Required:
            - sourced_id (str): The sourcedId of the category (path parameter)
            - category (TimebackCategory): Category data to update/create. See TimebackCategory for structure.
    """
    
    model_config = ConfigDict(populate_by_name=True)

    sourced_id: str = Field(..., description="The sourcedId of the category (path parameter)")
    category: TimebackCategory = Field(..., description="Category data")

