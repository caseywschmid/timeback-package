"""Response model for searching QTI stimuli.

GET /stimuli

Used by:
- timeback/services/qti/endpoints/search_stimuli.py
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from timeback.models.timeback_qti_stimulus import TimebackQTIStimulus
from timeback.enums import TimebackSortOrder


class TimebackSearchStimuliResponse(BaseModel):
    """Response model for searching QTI stimuli.
    
    Paginated response containing all stimuli that match the search criteria
    with navigation metadata.
    
    Attributes:
        - items (list): List of stimuli matching the search criteria.
          See TimebackQTIStimulus for structure.
        - total (int): Total number of entities matching the search criteria
        - page (int): Current page number (1-indexed)
        - pages (int): Total number of pages
        - limit (int): Number of entities per page
        - sort (str, optional): Field the results are sorted by
        - order (str): Sort order (asc or desc)
    """
    
    items: List[TimebackQTIStimulus] = Field(
        ...,
        description="List of stimuli matching the search criteria"
    )
    total: int = Field(
        ...,
        description="Total number of entities matching the search criteria"
    )
    page: int = Field(
        default=1,
        description="Current page number (1-indexed)"
    )
    pages: int = Field(
        ...,
        description="Total number of pages"
    )
    limit: int = Field(
        default=10,
        description="Number of entities per page"
    )
    sort: Optional[str] = Field(
        None,
        description="Field the results are sorted by"
    )
    order: TimebackSortOrder = Field(
        ...,
        description="Sort order (asc or desc)"
    )

