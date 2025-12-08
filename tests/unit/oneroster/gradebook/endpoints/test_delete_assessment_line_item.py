import pytest
from timeback.services.oneroster.gradebook.endpoints.delete_assessment_line_item import (
    delete_assessment_line_item,
)
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self, return_value=None):
        self.last_path = None
        self.return_value = return_value

    def delete(self, path):
        self.last_path = path
        return self.return_value


def test_delete_assessment_line_item_success_no_content():
    """Test successful deletion returning None (204 No Content)."""
    mock_http = MockHttp(return_value=None)
    result = delete_assessment_line_item(mock_http, "ali-001")
    
    assert result is None
    assert "/ims/oneroster/gradebook/v1p2/assessmentLineItems/ali-001" in mock_http.last_path


def test_delete_assessment_line_item_success_with_response():
    """Test successful deletion returning a response body."""
    response_body = {"assessmentLineItem": {"sourcedId": "ali-002", "status": "tobedeleted"}}
    mock_http = MockHttp(return_value=response_body)
    result = delete_assessment_line_item(mock_http, "ali-002")
    
    assert result == response_body


def test_delete_assessment_line_item_not_found():
    """Test that NotFoundError propagates from HTTP client."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Assessment line item not found")
    
    with pytest.raises(NotFoundError):
        delete_assessment_line_item(MockHttpNotFound(), "nonexistent")

