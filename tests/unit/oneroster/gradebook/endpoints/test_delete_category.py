import pytest
from timeback.services.oneroster.gradebook.endpoints.delete_category import (
    delete_category,
)
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self, return_value=None):
        self.last_path = None
        self.return_value = return_value

    def delete(self, path):
        self.last_path = path
        return self.return_value


def test_delete_category_success_no_content():
    """Test successful category deletion returning None (204 No Content)."""
    mock_http = MockHttp(return_value=None)
    result = delete_category(mock_http, "category-123")
    
    assert result is None
    assert "/ims/oneroster/gradebook/v1p2/categories/category-123" in mock_http.last_path


def test_delete_category_success_with_response():
    """Test successful category deletion returning a response body."""
    response_body = {"category": {"sourcedId": "category-456", "status": "tobedeleted"}}
    mock_http = MockHttp(return_value=response_body)
    result = delete_category(mock_http, "category-456")
    
    assert result == response_body
    assert "/ims/oneroster/gradebook/v1p2/categories/category-456" in mock_http.last_path


def test_delete_category_not_found():
    """Test that NotFoundError propagates from HTTP client."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Category not found")
    
    with pytest.raises(NotFoundError):
        delete_category(MockHttpNotFound(), "nonexistent-category")

