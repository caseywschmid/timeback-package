"""Create Lesson Plan endpoint for PowerPath.

POST /powerpath/lessonPlans/

Creates a new lesson plan for a course and student. If a lesson plan already
exists for the course/student combination, returns the existing lesson plan ID.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateLessonPlanRequest
from timeback.models.response import TimebackCreateLessonPlanResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def create_lesson_plan(
    http: HttpClient,
    request: TimebackCreateLessonPlanRequest,
) -> TimebackCreateLessonPlanResponse:
    """Create a new lesson plan for a course and student.

    POST /powerpath/lessonPlans/

    If the lesson plan already exists, returns the existing lesson plan ID (HTTP 200).
    If newly created, returns the new lesson plan ID (HTTP 201).

    Args:
        http: Injected HTTP client for making requests
        request: Request containing courseId, userId, and optional classId

    Returns:
        TimebackCreateLessonPlanResponse containing the lesson plan ID
    """
    path = "/powerpath/lessonPlans/"

    # Build request body using aliases for camelCase
    body: Dict[str, Any] = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackCreateLessonPlanResponse.model_validate(data)

