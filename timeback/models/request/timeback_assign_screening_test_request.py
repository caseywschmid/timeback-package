"""Request model for assigning a screening test.

POST /powerpath/screening/tests/assign
"""

from pydantic import BaseModel, Field
from typing import Literal


class TimebackAssignScreeningTestRequest(BaseModel):
    """Request model for assigning a screening test to a user.
    
    Assigns a screening test for a specific subject to a user. The response
    returns the updated screening session with assignment details.
    
    Attributes:
        Required:
            - userId (str): The sourcedId of the user to assign the test to
            - subject (Literal): The subject for the screening test.
              Valid values: "Math", "Reading", "Language", "Science"
              
    Note: The subject enum for screening tests is more limited than 
    placement tests - only Math, Reading, Language, and Science are supported.
    """

    userId: str = Field(..., description="The sourcedId of the user")
    subject: Literal["Math", "Reading", "Language", "Science"] = Field(
        ..., description="The subject name for the screening test"
    )

