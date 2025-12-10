"""Get Stimulus endpoint for QTI API.

GET /stimuli/{identifier}

Get a specific stimulus by identifier from the service provider.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetStimulusResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_stimulus(
    http: HttpClient,
    identifier: str
) -> TimebackGetStimulusResponse:
    """Get a specific QTI stimulus by identifier.
    
    GET /stimuli/{identifier}
    
    Retrieves a single stimulus with its complete content from the service provider.
    Stimuli can be referenced by assessment items to display relevant content.
    
    Steps:
        1. Build URL path with identifier
        2. Send GET request to /stimuli/{identifier}
        3. Parse and validate response as TimebackGetStimulusResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        identifier: Unique identifier of the stimulus to retrieve
    
    Returns:
        TimebackGetStimulusResponse containing the complete stimulus data
    
    Raises:
        HTTPError: If the request fails (404 if stimulus not found)
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> stimulus = get_stimulus(http, "stimulus-science-001")
        >>> print(stimulus.title, stimulus.raw_xml[:100])
    """
    path = f"/stimuli/{identifier}"
    
    log.debug(f"Getting stimulus: {identifier}")
    
    data: Dict[str, Any] = http.get(path)
    log.debug(f"Retrieved stimulus: {data.get('identifier')}")
    
    return TimebackGetStimulusResponse.model_validate(data)

