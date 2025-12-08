import pytest
from timeback.services.oneroster.gradebook.endpoints.delete_assessment_result import (
    delete_assessment_result,
)
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self, return_value=None):
        self.last_path = None
        self.return_value = return_value

    def delete(self, path):
        self.last_path = path
        return self.return_value


def test_delete_assessment_result_success_no_content():
    """Test successful assessment result deletion returning None (204 No Content)."""
    mock_http = MockHttp(return_value=None)
    result = delete_assessment_result(mock_http, "ar-001")
    
    assert result is None
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-001" in mock_http.last_path


def test_delete_assessment_result_success_with_response():
    """Test successful assessment result deletion returning a response body."""
    response_body = {"assessmentResult": {"sourcedId": "ar-002", "status": "tobedeleted"}}
    mock_http = MockHttp(return_value=response_body)
    result = delete_assessment_result(mock_http, "ar-002")
    
    assert result == response_body
    assert "/ims/oneroster/gradebook/v1p2/assessmentResults/ar-002" in mock_http.last_path


def test_delete_assessment_result_not_found():
    """Test that NotFoundError propagates from HTTP client."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Assessment result not found")
    
    with pytest.raises(NotFoundError):
        delete_assessment_result(MockHttpNotFound(), "nonexistent-ar")

