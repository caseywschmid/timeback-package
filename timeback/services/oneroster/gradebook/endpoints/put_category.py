"""Put Category endpoint for OneRoster Gradebook.

PUT /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

Updates or creates a category with the given sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackPutCategoryRequest
from timeback.models.response import TimebackPutCategoryResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def put_category(
    http: HttpClient, request: TimebackPutCategoryRequest
) -> TimebackPutCategoryResponse:
    """Update or create a category.

    PUT /ims/oneroster/gradebook/v1p2/categories/{sourcedId}

    Args:
        http: Injected HTTP client for making requests
        request: Request containing sourced_id and category data

    Returns:
        TimebackPutCategoryResponse containing the updated/created category
    """
    # Exclude sourced_id from body since it's used in the URL path
    body: Dict[str, Any] = request.model_dump(exclude_none=True, exclude={'sourced_id'}, by_alias=True)
    log.debug(f"PUT body: {body}")
    log.debug(f"Sourced ID: {request.sourced_id}")
    
    data: Dict[str, Any] = http.put(
        f"/ims/oneroster/gradebook/v1p2/categories/{request.sourced_id}", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackPutCategoryResponse.model_validate(data)

