"""Delete Course endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/courses/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_course(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a course (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/courses/{sourcedId}
    """
    log.debug(f"Deleting course: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/courses/{sourced_id}")

