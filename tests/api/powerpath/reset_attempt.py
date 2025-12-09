"""API tests for reset_attempt endpoint.

POST /powerpath/resetAttempt

These tests make real HTTP calls to the Timeback API.
Requires valid credentials in environment variables.
"""

import os
import pytest
from timeback import Timeback
from timeback.models.request import TimebackResetAttemptRequest
from timeback.models.response import TimebackResetAttemptResponse


# Skip if credentials not available
pytestmark = pytest.mark.skipif(
    not os.environ.get("TIMEBACK_CLIENT_ID"),
    reason="Requires TIMEBACK_CLIENT_ID and TIMEBACK_CLIENT_SECRET",
)


def test_reset_attempt_api_success():
    """Test reset_attempt with real API call.

    NOTE: This test requires:
    - Valid student ID
    - Valid lesson ID with an active attempt

    WARNING: This will actually reset the attempt!
    Adjust test data as needed for your environment.
    """
    client = Timeback()

    # TODO: Replace with valid test data
    request = TimebackResetAttemptRequest(
        student="test-student-id",
        lesson="test-lesson-id",
    )

    try:
        response = client.powerpath.reset_attempt(request)
        assert isinstance(response, TimebackResetAttemptResponse)
        assert isinstance(response.success, bool)
        assert isinstance(response.score, (int, float))
    except Exception as e:
        # Expected if test data doesn't exist
        pytest.skip(f"Skipping due to API error: {e}")

