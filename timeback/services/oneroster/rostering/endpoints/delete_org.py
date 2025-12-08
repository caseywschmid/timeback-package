"""Delete Org endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_org(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete an org (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/orgs/{sourcedId}
    """
    log.debug(f"Deleting org: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/orgs/{sourced_id}")

