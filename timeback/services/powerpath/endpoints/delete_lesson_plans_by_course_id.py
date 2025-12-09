"""Delete Lesson Plans by Course ID endpoint for PowerPath.

DELETE /powerpath/lessonPlans/{courseId}/deleteAll

Deletes all lesson plans for a course.
"""

from timeback.http import HttpClient
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def delete_lesson_plans_by_course_id(
    http: HttpClient,
    course_id: str,
) -> None:
    """Delete all lesson plans for a course.

    DELETE /powerpath/lessonPlans/{courseId}/deleteAll

    This is a destructive operation that removes all lesson plans
    associated with the specified course.

    Args:
        http: Injected HTTP client for making requests
        course_id: The sourcedId of the course

    Returns:
        None (HTTP 204 - no content)
    """
    path = f"/powerpath/lessonPlans/{course_id}/deleteAll"

    http.delete(path)
    log.debug(f"Deleted all lesson plans for course: {course_id}")
    # Returns None since the API responds with 204 No Content

