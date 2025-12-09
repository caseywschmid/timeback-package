"""List Student Test Assignments endpoint for PowerPath.

GET /powerpath/test-assignments

Returns test assignments for a specific student.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.response import TimebackListTestAssignmentsResponse
from timeback.enums import TimebackSubject, TimebackGrade
from timeback.models.timeback_test_assignment import TimebackTestAssignmentStatus
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def list_student_test_assignments(
    http: HttpClient,
    student: str,
    limit: int = 100,
    offset: int = 0,
    status: Optional[TimebackTestAssignmentStatus] = None,
    subject: Optional[TimebackSubject] = None,
    grade: Optional[TimebackGrade] = None,
) -> TimebackListTestAssignmentsResponse:
    """List test assignments for a student.

    GET /powerpath/test-assignments

    Returns a paginated list filtered by student with optional
    filters for status, subject, and grade.

    Args:
        http: Injected HTTP client for making requests
        student: The sourcedId of the student (required)
        limit: Max items to return (1-3000, default 100)
        offset: Items to skip (default 0)
        status: Optional status filter
        subject: Optional subject filter
        grade: Optional grade filter

    Returns:
        TimebackListTestAssignmentsResponse with assignments and pagination
    """
    path = "/powerpath/test-assignments"

    params: Dict[str, Any] = {
        "student": student,
        "limit": limit,
        "offset": offset,
    }

    if status is not None:
        params["status"] = status.value
    if subject is not None:
        params["subject"] = subject.value
    if grade is not None:
        params["grade"] = grade.value

    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Raw Data: {data}")
    return TimebackListTestAssignmentsResponse.model_validate(data)

