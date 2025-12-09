"""Create External Placement Test endpoint for PowerPath.

POST /powerpath/createExternalPlacementTest

Creates or updates a ComponentResource to act as a Placement Test lesson in a course.
This allows integrating with external test-taking platforms (like Edulastic) for content delivery.

The endpoint creates or updates:
- A CourseComponent for the course to hold the Placement Test lesson
- A Resource with lessonType = "placement" and the external service details as metadata
- A ComponentResource acting as the Placement Test lesson
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateExternalPlacementTestRequest
from timeback.models.response import TimebackCreateExternalTestResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_external_placement_test(
    http: HttpClient,
    request: TimebackCreateExternalPlacementTestRequest,
) -> TimebackCreateExternalTestResponse:
    """Create an external placement test for a course.

    POST /powerpath/createExternalPlacementTest

    Args:
        http: Injected HTTP client for making requests
        request: Request containing course info, tool provider, grades, and optional metadata

    Returns:
        TimebackCreateExternalTestResponse containing lessonId, courseComponentId, resourceId, etc.
    """
    path = "/powerpath/createExternalPlacementTest"

    # Build request body, excluding None values
    body: Dict[str, Any] = request.model_dump(exclude_none=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateExternalTestResponse.model_validate(data)

