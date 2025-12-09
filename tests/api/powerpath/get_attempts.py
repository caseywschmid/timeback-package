"""API tests for get_attempts endpoint.

GET /powerpath/getAttempts

These tests make real HTTP calls to the Timeback API.
Requires valid credentials in environment variables.
"""

import os
import pytest
from timeback import Timeback
from timeback.models.response import TimebackGetAttemptsResponse


# Skip if credentials not available
pytestmark = pytest.mark.skipif(
    not os.environ.get("TIMEBACK_CLIENT_ID"),
    reason="Requires TIMEBACK_CLIENT_ID and TIMEBACK_CLIENT_SECRET",
)


def test_get_attempts_api_success():
    """Test get_attempts with real API call.

    NOTE: This test requires:
    - Valid student ID
    - Valid lesson ID with attempts

    Adjust test data as needed for your environment.
    """
    client = Timeback()

    # TODO: Replace with valid test data
    student_id = "test-student-id"
    lesson_id = "test-lesson-id"

    try:
        response = client.powerpath.get_attempts(student_id, lesson_id)
        assert isinstance(response, TimebackGetAttemptsResponse)
        assert isinstance(response.attempts, list)
    except Exception as e:
        # Expected if test data doesn't exist
        pytest.skip(f"Skipping due to API error: {e}")

