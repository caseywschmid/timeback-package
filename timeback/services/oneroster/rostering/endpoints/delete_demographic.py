"""Delete Demographic endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_demographic(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a demographic (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/demographics/{sourcedId}
    """
    log.debug(f"Deleting demographic: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/demographics/{sourced_id}")

