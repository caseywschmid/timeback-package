"""Update Student Item Response endpoint for PowerPath.

POST /powerpath/lessonPlans/updateStudentItemResponse

Updates the student's response for a component or resource.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateStudentItemResponseRequest
from timeback.models.response import TimebackUpdateStudentItemResponseResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_student_item_response(
    http: HttpClient,
    request: TimebackUpdateStudentItemResponseRequest,
) -> TimebackUpdateStudentItemResponseResponse:
    """Update the student item response.

    POST /powerpath/lessonPlans/updateStudentItemResponse

    Updates the student's response for a component or resource with
    score information, status, and optional learning objective results.

    Args:
        http: Injected HTTP client for making requests
        request: Request with studentId, componentResourceId, and result

    Returns:
        TimebackUpdateStudentItemResponseResponse with line item and result
    """
    path = "/powerpath/lessonPlans/updateStudentItemResponse"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackUpdateStudentItemResponseResponse.model_validate(data)

