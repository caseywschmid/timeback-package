"""Get Course Progress endpoint for PowerPath.

GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}

Returns assessment line items and test-out status for a student in a course.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.response import TimebackCourseProgressResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_course_progress(
    http: HttpClient,
    course_id: str,
    student_id: str,
    lesson_id: Optional[str] = None,
) -> TimebackCourseProgressResponse:
    """Get course progress for a student.

    GET /powerpath/lessonPlans/getCourseProgress/{courseId}/student/{studentId}

    Returns assessment line items for the course and student:
    - type "component" indicates a unit or lesson
    - type "resource" indicates a video, quiz, document, etc.

    Each line item contains assessment results in the results attribute.

    Args:
        http: Injected HTTP client for making requests
        course_id: The sourcedId of the course
        student_id: The sourcedId of the student
        lesson_id: Optional component resource ID to filter by lesson

    Returns:
        TimebackCourseProgressResponse with lineItems and testOut status
    """
    path = f"/powerpath/lessonPlans/getCourseProgress/{course_id}/student/{student_id}"

    params: Dict[str, str] = {}
    if lesson_id:
        params["lessonId"] = lesson_id

    data: Dict[str, Any] = http.get(path, params=params if params else None)
    log.debug(f"Raw Data: {data}")
    return TimebackCourseProgressResponse.model_validate(data)

