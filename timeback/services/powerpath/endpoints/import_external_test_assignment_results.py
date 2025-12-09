"""Import External Test Assignment Results endpoint for PowerPath.

GET /powerpath/importExternalTestAssignmentResults

Retrieves and stores the results of an external test assignment.
Applies to 'test-out', 'placement', and 'unit-test' lessons.

The behavior varies by tool provider:
- For "edulastic": Imports results when all questions answered and grade is "GRADED"
- For "mastery-track": Imports results when scoreStatus is "fully graded"
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackImportExternalTestAssignmentResultsRequest
from timeback.models.response import TimebackImportExternalTestAssignmentResultsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def import_external_test_assignment_results(
    http: HttpClient,
    request: TimebackImportExternalTestAssignmentResultsRequest,
) -> TimebackImportExternalTestAssignmentResultsResponse:
    """Import results from an external test assignment.

    GET /powerpath/importExternalTestAssignmentResults

    Args:
        http: Injected HTTP client for making requests
        request: Request containing student sourcedId, lesson sourcedId, and optional applicationName

    Returns:
        TimebackImportExternalTestAssignmentResultsResponse with finalized status, credentials, etc.
    """
    path = "/powerpath/importExternalTestAssignmentResults"

    # Build query parameters from request
    query: Dict[str, Any] = {
        "student": request.student,
        "lesson": request.lesson,
    }
    if request.applicationName:
        query["applicationName"] = request.applicationName

    data: Dict[str, Any] = http.get(path, params=query)
    log.debug(f"Raw Data: {data}")
    return TimebackImportExternalTestAssignmentResultsResponse.model_validate(data)

