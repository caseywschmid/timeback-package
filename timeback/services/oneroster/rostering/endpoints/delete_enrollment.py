"""Delete Enrollment endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_enrollment(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete an enrollment (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/enrollments/{sourcedId}
    """
    log.debug(f"Deleting enrollment: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/enrollments/{sourced_id}")

