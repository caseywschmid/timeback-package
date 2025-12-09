"""Recreate Lesson Plan endpoint for PowerPath.

POST /powerpath/lessonPlans/{lessonPlanId}/recreate

Recreates a lesson plan from scratch using its operation log.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackSyncOperationsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def recreate_lesson_plan(
    http: HttpClient,
    lesson_plan_id: str,
) -> TimebackSyncOperationsResponse:
    """Recreate a lesson plan from scratch.

    POST /powerpath/lessonPlans/{lessonPlanId}/recreate

    Use when a lesson plan becomes corrupted or out of sync.
    This will:
    - Delete all current lesson plan items
    - Rebuild from the base course structure
    - Apply all operations from the operation log in sequence

    Args:
        http: Injected HTTP client for making requests
        lesson_plan_id: The ID of the lesson plan

    Returns:
        TimebackSyncOperationsResponse with success status and operation results
    """
    path = f"/powerpath/lessonPlans/{lesson_plan_id}/recreate"

    data: Dict[str, Any] = http.post(path)
    log.debug(f"Raw Data: {data}")
    return TimebackSyncOperationsResponse.model_validate(data)

