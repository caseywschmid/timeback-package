"""Response model for getting all assessment line items.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/assessmentLineItems

Per spec: HTTP 200 with paginated list of assessment line items.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackGetAllAssessmentLineItemsResponse(BaseModel):
    """Response model for paginated assessment line items list.

    Mirrors OneRoster list response envelope for assessment line items.
    
    Attributes:
        - assessmentLineItems (List[LineItem]): List of assessment line items. See LineItem for structure.
        - total_count (int): Total number of assessment line items
        - page_count (int): Total number of pages
        - page_number (int): Current page number
        - offset (int): Offset for pagination
        - limit (int): Limit per page
    """

    assessmentLineItems: List[LineItem] = Field(..., description="List of assessment line items")
    total_count: int = Field(..., description="Total number of assessment line items", alias="totalCount")
    page_count: int = Field(..., description="Total number of pages", alias="pageCount")
    page_number: int = Field(..., description="Current page number", alias="pageNumber")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

