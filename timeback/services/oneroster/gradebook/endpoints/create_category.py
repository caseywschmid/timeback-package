"""Create Category endpoint for OneRoster Gradebook.

POST /ims/oneroster/gradebook/v1p2/categories

Creates a new category and returns the allocated sourcedId.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateCategoryRequest
from timeback.models.response import TimebackCreateCategoryResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_category(
    http: HttpClient, request: TimebackCreateCategoryRequest
) -> TimebackCreateCategoryResponse:
    """Create a new category.

    POST /ims/oneroster/gradebook/v1p2/categories

    Args:
        http: Injected HTTP client for making requests
        request: Request containing category data to create

    Returns:
        TimebackCreateCategoryResponse containing sourcedId mapping
    """
    body: Dict[str, Any] = request.model_dump(by_alias=True, exclude_none=True)
    log.debug(f"POST body: {body}")
    
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/gradebook/v1p2/categories", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    return TimebackCreateCategoryResponse.model_validate(data)

