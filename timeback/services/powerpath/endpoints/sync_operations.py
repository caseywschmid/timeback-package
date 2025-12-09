"""Sync Operations endpoint for PowerPath.

POST /powerpath/lessonPlans/{lessonPlanId}/operations/sync

Applies pending operations to update the lesson plan structure.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackSyncOperationsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def sync_operations(
    http: HttpClient,
    lesson_plan_id: str,
) -> TimebackSyncOperationsResponse:
    """Sync pending operations for a lesson plan.

    POST /powerpath/lessonPlans/{lessonPlanId}/operations/sync

    Finds operations that haven't been applied yet, executes them
    in sequence, and updates the lesson plan structure.

    Args:
        http: Injected HTTP client for making requests
        lesson_plan_id: The ID of the lesson plan

    Returns:
        TimebackSyncOperationsResponse with success status and operation results
    """
    path = f"/powerpath/lessonPlans/{lesson_plan_id}/operations/sync"

    data: Dict[str, Any] = http.post(path)
    log.debug(f"Raw Data: {data}")
    return TimebackSyncOperationsResponse.model_validate(data)

