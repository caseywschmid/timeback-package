"""Update Stimulus endpoint for QTI API.

PUT /stimuli/{identifier}

Update an existing stimulus on the service provider.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackUpdateStimulusRequest
from timeback.models.response import TimebackUpdateStimulusResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def update_stimulus(
    http: HttpClient,
    request: TimebackUpdateStimulusRequest
) -> TimebackUpdateStimulusResponse:
    """Update an existing QTI stimulus.
    
    PUT /stimuli/{identifier}
    
    Updates a stimulus on the service provider with new content.
    
    Steps:
        1. Extract identifier from request for URL path
        2. Serialize remaining request fields to JSON body
        3. Send PUT request to /stimuli/{identifier}
        4. Parse and validate response as TimebackUpdateStimulusResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: Stimulus update data. The identifier field is used for the URL path.
                 See TimebackUpdateStimulusRequest for all available fields.
    
    Returns:
        TimebackUpdateStimulusResponse containing the updated stimulus with
        refreshed rawXml and updatedAt timestamp
    
    Raises:
        HTTPError: If the request fails (404 if stimulus not found, 400 for invalid data)
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackUpdateStimulusRequest(
        ...     identifier="stimulus-science-001",
        ...     title="Updated Forest Ecosystem",
        ...     content="<div><h2>Forest Ecosystems</h2><p>Updated content...</p></div>"
        ... )
        >>> response = update_stimulus(http, request)
        >>> print(response.updated_at)
    """
    path = f"/stimuli/{request.identifier}"
    
    # Serialize request body with aliases, excluding None values
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Updating stimulus: {request.identifier}")
    
    data: Dict[str, Any] = http.put(path, json=body)
    log.debug(f"Stimulus updated: {data.get('identifier')}")
    
    return TimebackUpdateStimulusResponse.model_validate(data)

