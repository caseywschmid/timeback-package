"""Create Stimulus endpoint for QTI API.

POST /stimuli

Create a new stimulus on the service provider. Stimuli can be referenced
by Assessment Items and provide shared content/passages.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateStimulusRequest
from timeback.models.response import TimebackCreateStimulusResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_stimulus(
    http: HttpClient,
    request: TimebackCreateStimulusRequest
) -> TimebackCreateStimulusResponse:
    """Create a new QTI stimulus.
    
    POST /stimuli
    
    Creates a new stimulus on the service provider. The stimulus can then
    be referenced by assessment items.
    
    Steps:
        1. Serialize request to JSON body with proper field aliases
        2. Send POST request to /stimuli endpoint
        3. Parse and validate response as TimebackCreateStimulusResponse
    
    Args:
        http: Injected HTTP client for making requests to the QTI API
        request: Stimulus data including identifier, title, and content.
                 See TimebackCreateStimulusRequest for all available fields.
    
    Returns:
        TimebackCreateStimulusResponse containing the created stimulus with:
            - All provided fields
            - Server-generated rawXml
            - Timestamps (createdAt, updatedAt)
    
    Raises:
        HTTPError: If the request fails (400 for invalid data, 409 for duplicate)
        ValidationError: If the response cannot be parsed
    
    Example:
        >>> request = TimebackCreateStimulusRequest(
        ...     identifier="stimulus-science-001",
        ...     title="Forest Ecosystem",
        ...     content="<div><h2>Forest Ecosystems</h2><p>Content...</p></div>",
        ...     metadata={"subject": "Science", "grade": "7"}
        ... )
        >>> response = create_stimulus(http, request)
        >>> print(response.identifier, response.raw_xml)
    """
    path = "/stimuli"
    
    # Serialize request body with aliases (e.g., catalogInfo instead of catalog_info)
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    
    log.debug(f"Creating stimulus with identifier: {request.identifier}")
    
    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Stimulus created: {data.get('identifier')}")
    
    return TimebackCreateStimulusResponse.model_validate(data)

