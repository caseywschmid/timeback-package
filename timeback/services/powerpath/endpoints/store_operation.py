"""Store Operation endpoint for PowerPath.

POST /powerpath/lessonPlans/{lessonPlanId}/operations

Stores a new operation in a lesson plan's operation log.
Primary endpoint for all lesson plan modifications.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackStoreOperationRequest
from timeback.models.response import TimebackStoreOperationResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def store_operation(
    http: HttpClient,
    request: TimebackStoreOperationRequest,
) -> TimebackStoreOperationResponse:
    """Store an operation on a lesson plan.

    POST /powerpath/lessonPlans/{lessonPlanId}/operations

    Available operation types:
    - set-skipped: Show/hide content for the student
    - move-item-before: Move item before another item
    - move-item-after: Move item after another item
    - move-item-to-start: Move item to start of parent
    - move-item-to-end: Move item to end of parent
    - add-custom-resource: Add a custom resource
    - change-item-parent: Move item to different parent

    Args:
        http: Injected HTTP client for making requests
        request: Request containing lessonPlanId, operation, and optional reason

    Returns:
        TimebackStoreOperationResponse with success status and operationId
    """
    path = f"/powerpath/lessonPlans/{request.lesson_plan_id}/operations"

    # Build request body
    body: Dict[str, Any] = {"operation": request.operation}
    if request.reason:
        body["reason"] = request.reason

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackStoreOperationResponse.model_validate(data)

