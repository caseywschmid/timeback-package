"""Reset User Placement endpoint for PowerPath.

POST /powerpath/placement/resetUserPlacement

Resets a user's placement progress for a specific subject by:
- Soft deleting all placement assessment results for that subject
- Resetting user onboarding state to "in_progress"

This operation is restricted to administrators only and cannot be undone.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackResetUserPlacementRequest
from timeback.models.response import TimebackResetUserPlacementResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def reset_user_placement(
    http: HttpClient,
    request: TimebackResetUserPlacementRequest,
) -> TimebackResetUserPlacementResponse:
    """Reset user placement progress for a subject.

    POST /powerpath/placement/resetUserPlacement

    This operation is restricted to administrators and cannot be undone.

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId and subject

    Returns:
        TimebackResetUserPlacementResponse with success status, deleted count, and reset flag
    """
    path = "/powerpath/placement/resetUserPlacement"

    # Build request body
    body: Dict[str, Any] = {
        "student": request.student,
        "subject": request.subject.value,
    }

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackResetUserPlacementResponse.model_validate(data)

