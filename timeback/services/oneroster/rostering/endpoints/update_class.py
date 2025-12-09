"""Update Class endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/classes/{sourcedId}

Updates an existing class.
"""

from typing import Dict, Any

from timeback.http import HttpClient
from timeback.models.request.timeback_update_class_request import (
    TimebackUpdateClassRequest,
)
from timeback.models.response import TimebackUpdateClassResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_class(
    http: HttpClient, request: TimebackUpdateClassRequest
) -> TimebackUpdateClassResponse:
    """Update an existing class.

    PUT /ims/oneroster/rostering/v1p2/classes/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing class data with sourcedId

    Returns:
        TimebackUpdateClassResponse containing the updated class
    """
    log.debug(f"Request: {request}")
    # Use by_alias=True to serialize 'class_' as 'class' in the JSON body
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)
    log.debug(f"PUT body: {body}")
    # Extract sourcedId from body for path parameter
    sourced_id = request.class_.sourcedId
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/classes/{sourced_id}", json=body
    )
    log.debug(f"Raw Data: {data}")
    return TimebackUpdateClassResponse.model_validate(data)

