"""Delete Stimulus endpoint for QTI API.

DELETE /stimuli/{identifier}

Permanently delete a stimulus from the service provider.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_stimulus(
    http: HttpClient,
    identifier: str
) -> None:
    """Delete a QTI stimulus.
    
    DELETE /stimuli/{identifier}
    
    Permanently deletes a stimulus from the service provider. This operation
    cannot be undone.
    
    Steps:
        1. Build URL path with identifier
        2. Send DELETE request to /stimuli/{identifier}
        3. Return None on success (204 No Content)
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: Unique identifier of the stimulus to delete
    
    Returns:
        None on successful deletion
    
    Raises:
        HTTPError: If the request fails (404 if stimulus not found)
    
    Warning:
        Assessment items that reference this stimulus may be affected.
        Consider checking for references before deletion.
    
    Example:
        >>> delete_stimulus(http, "stimulus-old-001")
        >>> # Stimulus is now permanently deleted
    """
    path = f"/stimuli/{identifier}"
    
    log.debug(f"Deleting stimulus: {identifier}")
    
    http.delete(path)
    
    log.debug(f"Stimulus deleted: {identifier}")

