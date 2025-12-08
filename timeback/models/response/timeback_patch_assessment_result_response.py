"""Response model for partially updating an assessment result.

Represents the body returned by:
- PATCH /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Per spec: HTTP 200 with updated assessmentResult object.
"""

from pydantic import BaseModel, Field
from timeback.models.timeback_assessment_result import TimebackAssessmentResult


class TimebackPatchAssessmentResultResponse(BaseModel):
    """Response model for PATCH assessment result.

    Attributes:
        - assessmentResult (TimebackAssessmentResult): The updated assessment result.
    """

    assessmentResult: TimebackAssessmentResult = Field(..., description="The updated assessment result")

