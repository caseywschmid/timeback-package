"""Request model for creating a Category.

POST /ims/oneroster/gradebook/v1p2/categories
"""

from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_category import TimebackCategory


class TimebackCreateCategoryRequest(BaseModel):
    """Top-level request wrapper for POST /categories.
    
    Attributes:
        Required:
            - category (TimebackCategory): Category data to create. See TimebackCategory for structure.
              Note: A 'title' field is required when creating a category.
    """
    
    model_config = ConfigDict(populate_by_name=True)

    category: TimebackCategory = Field(..., description="Category data to create")

