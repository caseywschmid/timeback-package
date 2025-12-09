"""Assign Screening Test endpoint for PowerPath.

POST /powerpath/screening/tests/assign

Assigns a screening test to a user for a specific subject.
Returns the updated screening session with assignment details.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackAssignScreeningTestRequest
from timeback.models import TimebackScreeningSession
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def assign_screening_test(
    http: HttpClient,
    request: TimebackAssignScreeningTestRequest,
) -> TimebackScreeningSession:
    """Assign a screening test to a user.

    POST /powerpath/screening/tests/assign

    Args:
        http: Injected HTTP client for making requests
        request: Request containing userId and subject

    Returns:
        TimebackScreeningSession containing updated session with assignment info
    """
    path = "/powerpath/screening/tests/assign"

    # Build request body
    body: Dict[str, Any] = {
        "userId": request.userId,
        "subject": request.subject,
    }

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackScreeningSession.model_validate(data)

