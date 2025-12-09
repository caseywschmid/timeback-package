"""Get Tree endpoint for PowerPath.

GET /powerpath/lessonPlans/{courseId}/{userId}

Returns the lesson plan tree for a course and student.
The tree contains nested components and resources representing the student's learning path.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetTreeRequest
from timeback.models import LessonPlan
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_tree(
    http: HttpClient,
    request: TimebackGetTreeRequest,
) -> LessonPlan:
    """Get the lesson plan tree for a course and student.

    GET /powerpath/lessonPlans/{courseId}/{userId}

    Returns the complete lesson plan tree including:
    - Course information
    - All components and subcomponents (units, lessons)
    - Component resources
    - Progress data

    Args:
        http: Injected HTTP client for making requests
        request: Request containing courseId and userId

    Returns:
        LessonPlan object with the complete tree structure
    """
    path = f"/powerpath/lessonPlans/{request.course_id}/{request.user_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")

    # Use from_dict to properly parse nested structure and components
    return LessonPlan.from_dict(data)

