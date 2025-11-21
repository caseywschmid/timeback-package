from typing import Dict, Any

from timeback.http import HttpClient
from timeback.models.request import TimebackCreateUserRequest
from timeback.models.response import TimebackCreateUserResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def create_user(http: HttpClient, request: TimebackCreateUserRequest) -> TimebackCreateUserResponse:
    """Create a new user.

    POST /ims/oneroster/rostering/v1p2/users/
    """
    body: Dict[str, Any] = request.model_dump(exclude_none=True)
    log.debug(f"POST body: {body}")
    data: Dict[str, Any] = http.post(
        "/ims/oneroster/rostering/v1p2/users/", json=body
    )
    log.debug(f"Raw Data: {data}")
    resp = TimebackCreateUserResponse.model_validate(data)
    return resp


