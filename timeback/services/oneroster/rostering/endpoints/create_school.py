"""Create School endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/schools

Creates a new school (organization).
"""

from typing import Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateSchoolRequest
from timeback.models.response import TimebackCreateSchoolResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_school(http: HttpClient, request: TimebackCreateSchoolRequest) -> TimebackCreateSchoolResponse:
    """Create a new school.

    POST /ims/oneroster/rostering/v1p2/schools

    Args:
        http: Injected HTTP client for making requests
        request: Request containing school data to create

    Returns:
        TimebackCreateSchoolResponse containing sourcedIdPairs mapping
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"POST body: {body}")
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/rostering/v1p2/schools", json=body
    )
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateSchoolResponse.model_validate(data)
    return resp

