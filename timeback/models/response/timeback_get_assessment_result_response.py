"""Response model for getting an assessment result.

Represents the body returned by:
- GET /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Per spec: HTTP 200 with assessmentResult object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_assessment_result import TimebackAssessmentResult


class TimebackGetAssessmentResultResponse(BaseModel):
    """Response model for getting a single assessment result.

    Attributes:
        - assessmentResult (TimebackAssessmentResult): The requested assessment result. See TimebackAssessmentResult for structure.
    """

    assessmentResult: TimebackAssessmentResult = Field(..., description="The requested assessment result")

