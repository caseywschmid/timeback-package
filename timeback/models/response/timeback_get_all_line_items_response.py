"""Response model for getting all line items.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/lineItems

Per spec: HTTP 200 with paginated list of line items.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.line_item import LineItem


class TimebackGetAllLineItemsResponse(BaseModel):
    """Response model for paginated line items list.

    Mirrors OneRoster list response envelope for line items.
    
    Attributes:
        - line_items (List[LineItem]): List of line items. See LineItem for structure.
        - total_count (int): Total number of line items
        - page_count (int): Total number of pages
        - page_number (int): Current page number
        - offset (int): Offset for pagination
        - limit (int): Limit per page
    """

    line_items: List[LineItem] = Field(..., description="List of line items", alias="lineItems")
    total_count: int = Field(..., description="Total number of line items", alias="totalCount")
    page_count: int = Field(..., description="Total number of pages", alias="pageCount")
    page_number: int = Field(..., description="Current page number", alias="pageNumber")
    offset: int = Field(..., description="Offset for pagination")
    limit: int = Field(..., description="Limit per page")

