import os
import pytest

from timeback import Timeback
from timeback.errors import NotFoundError
from timeback.models.request import TimebackGetUserRequest

# TODO: Replace with actual test user
# alannah.carrion@2hourlearning.com
TEST_SOURCED_ID = "31129aea-12b2-4e9e-a6e5-f5c8b712d674"


# TEST_SOURCED_ID = "REPLACE_WITH_ACTUAL_SOURCED_ID"
@pytest.mark.integration
def test_get_user_integration():
    """Integration test that calls the real TimeBack API.

    Requires environment variables:
    - TIMEBACK_CLIENT_ID
    - TIMEBACK_CLIENT_SECRET
    - TIMEBACK_ENVIRONMENT=production

    To run: pytest -m integration
    #"""
    # Check if required env vars are set
    required_vars = [
        "TIMEBACK_CLIENT_ID",
        "TIMEBACK_CLIENT_SECRET",
        "TIMEBACK_ENVIRONMENT",
    ]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        pytest.skip(f"Missing required environment variables: {missing_vars}")

    # Initialize client
    client = Timeback()

    # TODO: Replace with actual sourcedId provided by user
    test_sourced_id = TEST_SOURCED_ID

    if test_sourced_id == "REPLACE_WITH_ACTUAL_SOURCED_ID":
        pytest.skip("No test sourcedId provided - set test_sourced_id in this file")

    # Test the actual API call
    request = TimebackGetUserRequest(sourced_id=test_sourced_id)
    response = client.oneroster.rostering.get_user(request)

    # Verify we got a valid response with user object
    assert response is not None
    assert response.user is not None
    assert response.user.sourcedId == test_sourced_id
    assert response.user.givenName is not None
    assert response.user.familyName is not None
    assert response.user.enabledUser is not None
    assert response.user.status is not None
    assert response.user.roles is not None
    assert response.user.agents is not None
    assert response.user.userProfiles is not None

    print(
        f"Successfully fetched user: {response.user.givenName} {response.user.familyName} ({response.user.sourcedId})"
    )


@pytest.mark.integration
def test_get_user_integration_full_response():
    """Integration test ensuring full response returned (no filters)."""
    required_vars = [
        "TIMEBACK_CLIENT_ID",
        "TIMEBACK_CLIENT_SECRET",
        "TIMEBACK_ENVIRONMENT",
    ]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        pytest.skip(f"Missing required environment variables: {missing_vars}")

    client = Timeback()
    test_sourced_id = TEST_SOURCED_ID

    if test_sourced_id == "REPLACE_WITH_ACTUAL_SOURCED_ID":
        pytest.skip("No test sourcedId provided - set test_sourced_id in this file")

    request = TimebackGetUserRequest(sourced_id=test_sourced_id)
    response = client.oneroster.rostering.get_user(request)

    assert response.user.sourcedId == test_sourced_id
    assert response.user.enabledUser is not None
    assert response.user.roles is not None
    assert response.user.agents is not None
    assert response.user.userProfiles is not None


@pytest.mark.integration
def test_get_user_integration_not_found():
    """Integration test for 404 case."""
    required_vars = [
        "TIMEBACK_CLIENT_ID",
        "TIMEBACK_CLIENT_SECRET",
        "TIMEBACK_ENVIRONMENT",
    ]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        pytest.skip(f"Missing required environment variables: {missing_vars}")

    client = Timeback()

    # Use a non-existent sourcedId
    request = TimebackGetUserRequest(sourced_id="non-existent-sourced-id-12345")
    with pytest.raises(NotFoundError):
        client.oneroster.rostering.get_user(request)
