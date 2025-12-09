"""List All Test Assignments (Admin) endpoint for PowerPath.

GET /powerpath/test-assignments/admin

Returns all test assignments across students.
"""

from typing import Any, Dict, Optional

from timeback.http import HttpClient
from timeback.models.response import TimebackListTestAssignmentsResponse
from timeback.enums import TimebackSubject, TimebackGrade
from timeback.models.timeback_test_assignment import TimebackTestAssignmentStatus
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def list_all_test_assignments(
    http: HttpClient,
    limit: int = 100,
    offset: int = 0,
    student: Optional[str] = None,
    status: Optional[TimebackTestAssignmentStatus] = None,
    subject: Optional[TimebackSubject] = None,
    grade: Optional[TimebackGrade] = None,
) -> TimebackListTestAssignmentsResponse:
    """List all test assignments (admin).

    GET /powerpath/test-assignments/admin

    Returns a paginated list of test assignments across students
    with optional filters.

    Args:
        http: Injected HTTP client for making requests
        limit: Max items to return (1-3000, default 100)
        offset: Items to skip (default 0)
        student: Optional student sourcedId filter
        status: Optional status filter
        subject: Optional subject filter
        grade: Optional grade filter

    Returns:
        TimebackListTestAssignmentsResponse with assignments and pagination
    """
    path = "/powerpath/test-assignments/admin"

    params: Dict[str, Any] = {
        "limit": limit,
        "offset": offset,
    }

    if student is not None:
        params["student"] = student
    if status is not None:
        params["status"] = status.value
    if subject is not None:
        params["subject"] = subject.value
    if grade is not None:
        params["grade"] = grade.value

    data: Dict[str, Any] = http.get(path, params=params)
    log.debug(f"Raw Data: {data}")
    return TimebackListTestAssignmentsResponse.model_validate(data)

