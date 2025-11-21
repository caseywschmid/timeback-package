"""Request model for creating results for an academic session for a class.

POST /ims/oneroster/gradebook/v1p2/classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results

The request body must include a results array with Result objects.
Each result must have: lineItem (with sourcedId), student (with sourcedId), scoreStatus, and scoreDate.
"""

from typing import List
from pydantic import BaseModel, Field
from timeback.models.request.timeback_create_result_request import TimebackCreateResultBody


class TimebackPostResultsForAcademicSessionForClassRequest(BaseModel):
    """Request model for POST /classes/{classSourcedId}/academicSessions/{academicSessionSourcedId}/results.
    
    Attributes:
        Required:
            - class_sourced_id (str): The sourcedId of the class (path parameter)
            - academic_session_sourced_id (str): The sourcedId of the academic session (path parameter)
            - results (List[TimebackCreateResultBody]): Array of result data to create. See TimebackCreateResultBody for structure.
    """
    
    class_sourced_id: str = Field(..., description="The sourcedId of the class (path parameter)")
    academic_session_sourced_id: str = Field(..., description="The sourcedId of the academic session (path parameter)")
    results: List[TimebackCreateResultBody] = Field(..., description="Array of result data to create")

