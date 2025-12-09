"""Delete Academic Session endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_academic_session(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete an academic session (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/academicSessions/{sourcedId}
    """
    log.debug(f"Deleting academic session: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/academicSessions/{sourced_id}")

