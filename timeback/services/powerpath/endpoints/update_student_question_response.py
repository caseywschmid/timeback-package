"""Update Student Question Response endpoint for PowerPath.

PUT /powerpath/updateStudentQuestionResponse

Updates a student's response to a question and returns updated scores.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateStudentQuestionResponseRequest
from timeback.models.response import TimebackUpdateStudentQuestionResponseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_student_question_response(
    http: HttpClient,
    request: TimebackUpdateStudentQuestionResponseRequest,
) -> TimebackUpdateStudentQuestionResponseResponse:
    """Update a student's response to a question.

    PUT /powerpath/updateStudentQuestionResponse

    Checks correctness using QTI response declarations and updates
    the score accordingly. Creates/updates AssessmentLineItem and
    AssessmentResult objects.

    Args:
        http: Injected HTTP client for making requests
        request: Request with student, question, lesson, and response(s)

    Returns:
        TimebackUpdateStudentQuestionResponseResponse with updated scores
    """
    path = "/powerpath/updateStudentQuestionResponse"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackUpdateStudentQuestionResponseResponse.model_validate(data)
