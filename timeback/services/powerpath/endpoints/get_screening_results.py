"""Get Screening Results endpoint for PowerPath.

GET /powerpath/screening/results/{userId}

Returns screening test results for a user across all subjects.
Each subject maps to either a result object or null if no result exists.
"""

from typing import Any, Dict

from timeback.http import HttpClient
from timeback.models.response import TimebackGetScreeningResultsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="INFO")


def get_screening_results(
    http: HttpClient,
    user_id: str,
) -> TimebackGetScreeningResultsResponse:
    """Fetch screening test results for a user.

    GET /powerpath/screening/results/{userId}

    Args:
        http: Injected HTTP client for making requests
        user_id: The sourcedId of the user to get screening results for

    Returns:
        TimebackGetScreeningResultsResponse - a dict mapping subject names to screening results
    """
    path = f"/powerpath/screening/results/{user_id}"

    data: Dict[str, Any] = http.get(path)
    log.debug(f"Raw Data: {data}")
    return TimebackGetScreeningResultsResponse.model_validate(data)

