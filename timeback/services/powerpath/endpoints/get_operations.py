"""Get Operations endpoint for PowerPath.

GET /powerpath/lessonPlans/{lessonPlanId}/operations

Returns all operations for a lesson plan in chronological order.
Used for audit trails, history tracking, and debugging.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetOperationsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_operations(
    http: HttpClient,
    lesson_plan_id: str,
) -> TimebackGetOperationsResponse:
    """Get all operations for a lesson plan.

    GET /powerpath/lessonPlans/{lessonPlanId}/operations

    Returns all operations in chronological order including:
    - Operation type and payload
    - Timestamp and sequence number
    - Who made the change and why

    Args:
        http: Injected HTTP client for making requests
        lesson_plan_id: The ID of the lesson plan

    Returns:
        TimebackGetOperationsResponse containing list of operations
    """
    path = f"/powerpath/lessonPlans/{lesson_plan_id}/operations"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackGetOperationsResponse.model_validate(data)

