"""Response model for getting course syllabus.

GET /powerpath/syllabus/{courseSourcedId}
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class TimebackSyllabusResponse(BaseModel):
    """Response model for getting course syllabus.
    
    Attributes:
        - syllabus (Any): The course syllabus content. Structure varies
          based on course configuration.
    """

    syllabus: Optional[Any] = Field(None, description="The course syllabus content")

