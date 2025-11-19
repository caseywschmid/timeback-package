"""Register Student Credentials endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials

Builds the full path with user_id from request, performs the HTTP POST via the injected
`HttpClient`, and returns the response as a TimebackRegisterStudentCredentialsResponse.
"""

from timeback.http import HttpClient
from timeback.models.request import TimebackRegisterStudentCredentialsRequest
from timeback.models.response import TimebackRegisterStudentCredentialsResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def register_student_credentials(
    http: HttpClient, request: TimebackRegisterStudentCredentialsRequest
) -> TimebackRegisterStudentCredentialsResponse:
    """Register student credentials for third-party applications.

    Args:
        http: Injected HTTP client for making requests
        request: Request containing user_id, application_name, and credentials

    Returns:
        TimebackRegisterStudentCredentialsResponse containing userProfileId, credentialId, and message
    """
    log.debug(f"Request: {request}")
    
    # Build request body from the credentials and application name
    body = {
        "applicationName": request.application_name,
        "credentials": {
            "username": request.credentials.username,
            "password": request.credentials.password,
        },
    }
    
    log.debug(f"POST body: {body}")
    
    # Make the POST request
    data = http.post(
        f"/ims/oneroster/rostering/v1p2/users/{request.user_id}/credentials", json=body
    )
    
    log.debug(f"Raw Data: {data}")
    
    # Return the validated response model
    return TimebackRegisterStudentCredentialsResponse.model_validate(data)
