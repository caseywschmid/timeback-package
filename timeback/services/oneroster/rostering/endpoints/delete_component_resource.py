"""Delete Component Resource endpoint for OneRoster Rostering.

DELETE /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
"""

from typing import Optional, Dict, Any
from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def delete_component_resource(http: HttpClient, sourced_id: str) -> Optional[Dict[str, Any]]:
    """Soft delete a component resource (sets status to 'tobedeleted').

    DELETE /ims/oneroster/rostering/v1p2/courses/component-resources/{sourcedId}
    """
    log.debug(f"Deleting component resource: {sourced_id}")
    return http.delete(f"/ims/oneroster/rostering/v1p2/courses/component-resources/{sourced_id}")

