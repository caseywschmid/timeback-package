"""Delete School endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/schools/{sourcedId}

Performs a soft delete on a specific school (sets status to 'tobedeleted').
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_school(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a school (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/schools/{sourcedId}
    
    Args:
        http: Injected HTTP client for making requests
        sourced_id: The sourcedId of the school to delete
    
    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for 204 No Content)
    """
    log.debug(f"Deleting school: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/schools/{sourced_id}")

