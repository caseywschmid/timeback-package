"""Response model for updating/creating an assessment result.

Represents the body returned by:
- PUT /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Per spec: HTTP 201 with assessmentResult object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_assessment_result import TimebackAssessmentResult


class TimebackPutAssessmentResultResponse(BaseModel):
    """Response model for PUT assessment result.

    Attributes:
        - assessmentResult (TimebackAssessmentResult): The updated/created assessment result.
    """

    assessmentResult: TimebackAssessmentResult = Field(..., description="The updated/created assessment result")

