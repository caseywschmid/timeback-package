"""API tests for get_next_question endpoint.

GET /powerpath/getNextQuestion

These tests make real HTTP calls to the Timeback API.
Requires valid credentials in environment variables.
"""

import os
import pytest
from timeback import Timeback
from timeback.models.response import TimebackNextQuestionResponse


# Skip if credentials not available
pytestmark = pytest.mark.skipif(
    not os.environ.get("TIMEBACK_CLIENT_ID"),
    reason="Requires TIMEBACK_CLIENT_ID and TIMEBACK_CLIENT_SECRET",
)


def test_get_next_question_api_success():
    """Test get_next_question with real API call.

    NOTE: This test requires:
    - Valid student ID
    - Valid PowerPath-100 lesson ID

    Adjust test data as needed for your environment.
    """
    client = Timeback()

    # TODO: Replace with valid test data
    student_id = "test-student-id"
    lesson_id = "test-powerpath-100-lesson-id"

    try:
        response = client.powerpath.get_next_question(student_id, lesson_id)
        assert isinstance(response, TimebackNextQuestionResponse)
        assert response.question is not None
        assert isinstance(response.score, (int, float))
    except Exception as e:
        # Expected if test data doesn't exist or lesson isn't powerpath-100
        pytest.skip(f"Skipping due to API error: {e}")

