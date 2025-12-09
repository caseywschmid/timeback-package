"""Update School endpoint for OneRoster Rostering.

PUT /ims/oneroster/rostering/v1p2/schools/{sourcedId}

Updates an existing school.
"""

from typing import Dict, Any

from timeback.http import HttpClient
from timeback.models.request.timeback_update_school_request import (
    TimebackUpdateSchoolRequest,
)
from timeback.models.response import TimebackUpdateSchoolResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def update_school(
    http: HttpClient, request: TimebackUpdateSchoolRequest
) -> TimebackUpdateSchoolResponse:
    """Update an existing school.

    PUT /ims/oneroster/rostering/v1p2/schools/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing school data with sourcedId

    Returns:
        TimebackUpdateSchoolResponse containing the updated school
    """
    log.debug(f"Request: {request}")
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"PUT body: {body}")
    # Extract sourcedId from body for path parameter
    sourced_id = request.org.sourcedId
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/rostering/v1p2/schools/{sourced_id}", json=body
    )
    log.debug(f"Raw Data: {data}")
    return TimebackUpdateSchoolResponse.model_validate(data)

