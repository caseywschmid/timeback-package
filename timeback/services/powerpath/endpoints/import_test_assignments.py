"""Import Test Assignments endpoint for PowerPath.

POST /powerpath/test-assignments/import

Imports test assignments from a Google Sheet.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.request import TimebackImportTestAssignmentsRequest
from timeback.models.response import TimebackBulkTestAssignmentsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def import_test_assignments(
    http: HttpClient,
    request: TimebackImportTestAssignmentsRequest,
) -> TimebackBulkTestAssignmentsResponse:
    """Import test assignments from Google Sheets.

    POST /powerpath/test-assignments/import

    Fetches a public Google Sheet tab as CSV and creates test
    assignments in bulk. Sheet must have columns: student, subject, grade.

    All-or-nothing operation.

    Args:
        http: Injected HTTP client for making requests
        request: Request with spreadsheetUrl and sheet name

    Returns:
        TimebackBulkTestAssignmentsResponse with success, results, errors
    """
    path = "/powerpath/test-assignments/import"

    body = request.model_dump(exclude_none=True, by_alias=True)

    data: Dict[str, Any] = http.post(path, json=body)
    log.debug(f"Raw Data: {data}")
    return TimebackBulkTestAssignmentsResponse.model_validate(data)

