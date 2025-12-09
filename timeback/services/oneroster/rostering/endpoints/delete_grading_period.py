"""Delete Grading Period endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_grading_period(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a grading period (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/gradingPeriods/{sourcedId}
    """
    log.debug(f"Deleting grading period: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/gradingPeriods/{sourced_id}")

