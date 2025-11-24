"""Response model for getting all classes.

Represents the body returned by:
- GET /ims/oneroster/rostering/v1p2/classes

Per spec: HTTP 200 with classes collection and pagination info.
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_class import TimebackClass


class TimebackGetAllClassesResponse(BaseModel):
    """Response model for getting all classes.

    Attributes:
        - classes (List[TimebackClass]): List of classes. See TimebackClass for structure.
        - total_count (int): Total number of records available.
        - page_count (int): Total number of pages.
        - page_number (int): Current page number.
        - offset (int): Current offset.
        - limit (int): Current limit.
    """

    model_config = ConfigDict(populate_by_name=True)

    classes: List[TimebackClass] = Field(..., alias="classes")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(..., alias="offset")
    limit: int = Field(..., alias="limit")

