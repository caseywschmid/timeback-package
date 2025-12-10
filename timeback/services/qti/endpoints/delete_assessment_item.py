"""Delete Assessment Item endpoint for QTI API.

DELETE /assessment-items/{identifier}

Permanently delete a QTI assessment item.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_assessment_item(
    http: HttpClient,
    identifier: str
) -> Optional[Dict[str, Any]]:
    """Delete a QTI assessment item.
    
    DELETE /assessment-items/{identifier}
    
    Permanently deletes an assessment item from the service provider.
    This operation cannot be undone.
    
    Warning: Assessment tests that reference this item may be affected.
    The item references in test sections will need to be updated separately.
    
    Steps:
        1. Build the path with the identifier
        2. Send DELETE request to /assessment-items/{identifier}
        3. Return None on success (HTTP 204)
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: The unique identifier of the assessment item to delete
    
    Returns:
        None if successful (HTTP 204), or a dictionary with response data
    
    Raises:
        HTTPError: If the request fails
        NotFoundError: If the assessment item doesn't exist
    
    Example:
        >>> delete_assessment_item(http, "item-001")
        >>> # Assessment item "item-001" is now deleted
    """
    path = f"/assessment-items/{identifier}"
    
    log.debug(f"Deleting assessment item: {identifier}")
    
    result = http.delete(path)
    
    log.debug(f"Deleted assessment item: {identifier}")
    
    return result

