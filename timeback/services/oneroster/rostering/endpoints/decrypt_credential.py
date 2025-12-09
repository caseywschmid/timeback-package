"""Decrypt Credential endpoint for OneRoster Rostering.

POST /ims/oneroster/rostering/v1p2/users/{userId}/credentials/{credentialId}/decrypt

Builds the full path with user_id and credential_id from request, performs the HTTP POST 
via the injected `HttpClient`, and returns the response as a TimebackDecryptCredentialResponse.
"""

from timeback.http import HttpClient
from timeback.models.request import TimebackDecryptCredentialRequest
from timeback.models.response import TimebackDecryptCredentialResponse
from timeback.logs import logger

log = logger.configure_logging(__name__, log_level="DEBUG")


def decrypt_credential(
    http: HttpClient, request: TimebackDecryptCredentialRequest
) -> TimebackDecryptCredentialResponse:
    """Decrypt and return the password for a specific user credential.

    Args:
        http: Injected HTTP client for making requests
        request: Request containing user_id and credential_id

    Returns:
        TimebackDecryptCredentialResponse containing the decrypted password
    """
    log.debug(f"Request: {request}")
    
    # Make the POST request (no body needed for this endpoint)
    data = http.post(
        f"/ims/oneroster/rostering/v1p2/users/{request.user_id}/credentials/{request.credential_id}/decrypt"
    )
    
    log.debug(f"Raw Data: {data}")
    
    # Return the validated response model
    return TimebackDecryptCredentialResponse.model_validate(data)
