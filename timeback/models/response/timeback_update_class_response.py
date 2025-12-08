"""Response model for updating a OneRoster Class.

Represents the body returned by:
- PUT /ims/oneroster/rostering/v1p2/classes/{sourcedId}
"""

from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_class import TimebackClass


class TimebackUpdateClassResponse(BaseModel):
    """Response model for updating a OneRoster Class.
    
    Attributes:
        - class_ (TimebackClass): Updated class object. See TimebackClass for structure.
          Note: The field is named 'class_' in Python to avoid keyword conflict,
          but maps to 'class' in the API response via alias.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    class_: TimebackClass = Field(..., description="Updated class object", alias="class")

