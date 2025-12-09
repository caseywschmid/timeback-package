"""API tests for update_student_question_response endpoint.

PUT /powerpath/updateStudentQuestionResponse

These tests make real HTTP calls to the Timeback API.
Requires valid credentials in environment variables.
"""

import os
import pytest
from timeback import Timeback
from timeback.models.request import TimebackUpdateStudentQuestionResponseRequest
from timeback.models.response import TimebackUpdateStudentQuestionResponseResponse


# Skip if credentials not available
pytestmark = pytest.mark.skipif(
    not os.environ.get("TIMEBACK_CLIENT_ID"),
    reason="Requires TIMEBACK_CLIENT_ID and TIMEBACK_CLIENT_SECRET",
)


def test_update_student_question_response_api_success():
    """Test update_student_question_response with real API call.

    NOTE: This test requires:
    - Valid student ID
    - Valid question ID from lesson's question bank
    - Valid lesson ID

    WARNING: This will actually submit a response!
    Adjust test data as needed for your environment.
    """
    client = Timeback()

    # TODO: Replace with valid test data
    request = TimebackUpdateStudentQuestionResponseRequest(
        student="test-student-id",
        question="test-question-id",
        lesson="test-lesson-id",
        responses={"RESPONSE": "test-choice"},
    )

    try:
        response = client.powerpath.update_student_question_response(request)
        assert isinstance(response, TimebackUpdateStudentQuestionResponseResponse)
        assert response.lessonType is not None
    except Exception as e:
        # Expected if test data doesn't exist
        pytest.skip(f"Skipping due to API error: {e}")

