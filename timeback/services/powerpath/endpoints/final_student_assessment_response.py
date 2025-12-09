"""Final Student Assessment Response endpoint for PowerPath.

POST /powerpath/finalStudentAssessmentResponse

Finalizes a test assessment after all questions have been answered.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackFinalStudentAssessmentRequest
from timeback.models.response import TimebackFinalStudentAssessmentResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def final_student_assessment_response(
    http: HttpClient,
    request: TimebackFinalStudentAssessmentRequest,
) -> TimebackFinalStudentAssessmentResponse:
    """Finalize a test assessment.

    POST /powerpath/finalStudentAssessmentResponse

    Finalizes a lesson of type quiz, test-out, or placement:
    - Evaluates answered questions
    - Attributes scores for each question and overall lesson
    - Creates/updates AssessmentLineItem and AssessmentResult objects
    - May trigger course enrollment for placement/test-out

    Not supported for external test lessons - use
    import_external_test_assignment_results instead.

    Args:
        http: Injected HTTP client for making requests
        request: Request with student and lesson IDs

    Returns:
        TimebackFinalStudentAssessmentResponse with finalization status
    """
    path = "/powerpath/finalStudentAssessmentResponse"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackFinalStudentAssessmentResponse.model_validate(data)

