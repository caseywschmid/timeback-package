"""Reset Screening Session endpoint for PowerPath.

POST /powerpath/screening/session/reset

Resets the screening session for a user.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def reset_screening_session(
    http: HttpClient,
    user_id: str,
) -> None:
    """Reset screening session for a user.

    POST /powerpath/screening/session/reset

    Args:
        http: Injected HTTP client for making requests
        user_id: The sourcedId of the user whose session to reset

    Returns:
        None (HTTP 204 - no content)
    """
    path = "/powerpath/screening/session/reset"

    body: Dict[str, Any] = {"userId": user_id}

    http.post(path, json=body)
    log.debug(f"Session reset for user: {user_id}")
    # Returns None since the API responds with 204 No Content

