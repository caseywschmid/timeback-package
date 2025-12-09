"""Delete Assessment Result endpoint for OneRoster Gradebook.

DELETE /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}

Performs a soft delete on a specific assessment result (sets status to 'tobedeleted').
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_assessment_result(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete an assessment result (sets status to 'tobedeleted').

    DELETE /ims/oneroster/gradebook/v1p2/assessmentResults/{sourcedId}
    
    Args:
        http: Injected HTTP client for making requests
        sourced_id: The sourcedId of the assessment result to delete
    
    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for 204 No Content)
    """
    log.debug(f"Deleting assessment result: {sourced_id}")
    return http.delete(f"/ims/oneroster/gradebook/v1p2/assessmentResults/{sourced_id}")

