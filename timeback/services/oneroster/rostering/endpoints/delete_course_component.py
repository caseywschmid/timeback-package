"""Delete Course Component endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_course_component(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a course component (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/courses/components/{sourcedId}
    """
    log.debug(f"Deleting course component: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/courses/components/{sourced_id}")

