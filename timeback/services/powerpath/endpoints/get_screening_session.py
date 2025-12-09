"""Get Screening Session endpoint for PowerPath.

GET /powerpath/screening/session/{userId}

Returns the screening session information for a user, including
NWEA credentials, session status, and assignment details.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models import TimebackScreeningSession
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_screening_session(
    http: HttpClient,
    user_id: str,
) -> TimebackScreeningSession:
    """Fetch the screening session for a user.

    GET /powerpath/screening/session/{userId}

    Args:
        http: Injected HTTP client for making requests
        user_id: The sourcedId of the user to get the screening session for

    Returns:
        TimebackScreeningSession containing session credentials, status, and assignment info
    """
    path = f"/powerpath/screening/session/{user_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackScreeningSession.model_validate(data)

