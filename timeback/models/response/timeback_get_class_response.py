"""Response model for getting a OneRoster Class.

Represents the body returned by:
- GET /ims/oneroster/rostering/v1p2/classes/{sourcedId}
"""

from pydantic import BaseModel, ConfigDict, Field
from timeback.models.timeback_class import TimebackClass


class TimebackGetClassResponse(BaseModel):
    """Response model for getting a OneRoster Class.
    
    Attributes:
        - class_ (TimebackClass): Class object. See TimebackClass for structure.
          Note: The field is named 'class_' in Python to avoid keyword conflict,
          but maps to 'class' in the API response via alias.
    """
    
    model_config = ConfigDict(populate_by_name=True)
    
    class_: TimebackClass = Field(..., description="Class object", alias="class")

