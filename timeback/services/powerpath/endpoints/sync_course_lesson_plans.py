"""Sync Course Lesson Plans endpoint for PowerPath.

POST /powerpath/lessonPlans/course/{courseId}/sync

Bulk synchronization of all lesson plans for a course.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackSyncCourseLessonPlansResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def sync_course_lesson_plans(
    http: HttpClient,
    course_id: str,
) -> TimebackSyncCourseLessonPlansResponse:
    """Sync all lesson plans for a course.

    POST /powerpath/lessonPlans/course/{courseId}/sync

    Use after making significant structural changes to a base course
    to ensure all students have the latest content.

    This will:
    - Find all lesson plans associated with the course
    - Recreate each from the base course structure
    - Apply all historical operations to maintain personalizations

    Args:
        http: Injected HTTP client for making requests
        course_id: The sourcedId of the course

    Returns:
        TimebackSyncCourseLessonPlansResponse with list of affected lesson plan IDs
    """
    path = f"/powerpath/lessonPlans/course/{course_id}/sync"

    data: Dict[str, Any] = http.post(path)
    log.debug(f"Raw Data: {data}")
    return TimebackSyncCourseLessonPlansResponse.model_validate(data)

