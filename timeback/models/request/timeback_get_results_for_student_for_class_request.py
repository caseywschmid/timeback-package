"""Request model for getting results for a student for a class.

GET /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/students/{studentSourcedId}/results
"""

from typing import Optional
from pydantic import BaseModel, Field

from timeback.models.request.timeback_query_params import TimebackQueryParams


class TimebackGetResultsForStudentForClassRequest(BaseModel):
    """Request model for getting results for a student for a class (paginated list).
    
    Attributes:
        Required:
            - class_sourced_id (str): The sourcedId of the class (path parameter)
            - student_sourced_id (str): The sourcedId of the student (path parameter)
        
        Optional:
            - query_params (TimebackQueryParams, optional): Query parameters for filtering, pagination, sorting, etc.
              See TimebackQueryParams for available options.
    """

    class_sourced_id: str = Field(..., description="The sourcedId of the class (path parameter)")
    student_sourced_id: str = Field(..., description="The sourcedId of the student (path parameter)")
    query_params: Optional[TimebackQueryParams] = Field(
        None, description="Optional query parameters (fields, limit, offset, sort, filter, search, etc.)"
    )

