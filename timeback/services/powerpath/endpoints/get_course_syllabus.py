"""Get Course Syllabus endpoint for PowerPath.

GET /powerpath/syllabus/{courseSourcedId}

Returns the syllabus for a course.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackSyllabusResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_course_syllabus(
    http: HttpClient,
    course_sourced_id: str,
) -> TimebackSyllabusResponse:
    """Get the syllabus for a course.

    GET /powerpath/syllabus/{courseSourcedId}

    Args:
        http: Injected HTTP client for making requests
        course_sourced_id: The sourcedId of the course

    Returns:
        TimebackSyllabusResponse with syllabus content
    """
    path = f"/powerpath/syllabus/{course_sourced_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackSyllabusResponse.model_validate(data)

