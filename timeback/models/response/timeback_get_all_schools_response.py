"""Response model for getting all schools.

Represents the body returned by:
- GET /ims/oneroster/rostering/v1p2/schools

Per spec: HTTP 200 with orgs collection and pagination info.
"""

from typing import List
from pydantic import BaseModel, Field, ConfigDict
from timeback.models.timeback_org import TimebackOrg


class TimebackGetAllSchoolsResponse(BaseModel):
    """Response model for getting all schools.

    Attributes:
        - orgs (List[TimebackOrg]): List of schools (organizations).
        - total_count (int): Total number of records available.
        - page_count (int): Total number of pages.
        - page_number (int): Current page number.
        - offset (int): Current offset.
        - limit (int): Current limit.
    """

    model_config = ConfigDict(populate_by_name=True)

    orgs: List[TimebackOrg] = Field(..., alias="orgs")
    total_count: int = Field(..., alias="totalCount")
    page_count: int = Field(..., alias="pageCount")
    page_number: int = Field(..., alias="pageNumber")
    offset: int = Field(..., alias="offset")
    limit: int = Field(..., alias="limit")
