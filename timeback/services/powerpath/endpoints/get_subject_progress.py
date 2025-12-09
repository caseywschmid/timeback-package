"""Get Subject Progress endpoint for PowerPath.

GET /powerpath/placement/getSubjectProgress

Returns the progress the student has made in the given subject,
including completion status for each course, XP earned, and test-out usage.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackGetSubjectProgressRequest
from timeback.models.response import TimebackGetSubjectProgressResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_subject_progress(
    http: HttpClient,
    request: TimebackGetSubjectProgressRequest,
) -> TimebackGetSubjectProgressResponse:
    """Fetch the progress a student has made in a subject.

    GET /powerpath/placement/getSubjectProgress

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId and subject

    Returns:
        TimebackGetSubjectProgressResponse containing progress for each course in the subject
    """
    path = "/powerpath/placement/getSubjectProgress"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "subject": request.subject.value,  # Convert enum to string value
    }

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackGetSubjectProgressResponse.model_validate(data)

