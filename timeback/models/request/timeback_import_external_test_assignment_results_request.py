"""Request model for importing external test assignment results.

GET /powerpath/importExternalTestAssignmentResults
"""

from typing import Optional
from pydantic import BaseModel, Field


class TimebackImportExternalTestAssignmentResultsRequest(BaseModel):
    """Request model for importing external test assignment results.
    
    Retrieves and stores the results of an external test assignment.
    Applies to 'test-out', 'placement', and 'unit-test' lessons.
    
    Attributes:
        Required:
            - student (str): The sourcedId of the student
            - lesson (str): The sourcedId of the lesson (ComponentResource)
            
        Optional:
            - applicationName (str): The name of the application
    """

    student: str = Field(..., description="The sourcedId of the student")
    lesson: str = Field(..., description="The sourcedId of the lesson (ComponentResource)")
    applicationName: Optional[str] = Field(None, description="The name of the application")

