"""Delete Resource endpoint for OneRoster Resources.

DELETE /ims/oneroster/resources/v1p2/resources/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_resource(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a resource (sets status to 'tobedeleted').

    DELETE /ims/oneroster/resources/v1p2/resources/{sourcedId}
    
    Returns:
        Optional[Dict[str, Any]]: Raw provider response (None for 204 No Content)
    """
    log.debug(f"Deleting resource: {sourced_id}")
    return http.delete(f"/ims/oneroster/resources/v1p2/resources/{sourced_id}")

