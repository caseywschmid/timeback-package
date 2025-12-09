import pytest
from timeback.services.oneroster.resources.endpoints.delete_resource import delete_resource
from timeback.errors import NotFoundError


class MockHttp:
    def __init__(self, return_value=None):
        self.last_path = None
        self.return_value = return_value

    def delete(self, path):
        self.last_path = path
        return self.return_value


def test_delete_resource_success_no_content():
    """Test successful deletion returning None (204 No Content)."""
    mock_http = MockHttp(return_value=None)
    result = delete_resource(mock_http, "res-001")
    
    assert result is None
    assert "/ims/oneroster/resources/v1p2/resources/res-001" in mock_http.last_path


def test_delete_resource_not_found():
    """Test that NotFoundError propagates from HTTP client."""
    class MockHttpNotFound:
        def delete(self, path):
            raise NotFoundError("Resource not found")
    
    with pytest.raises(NotFoundError):
        delete_resource(MockHttpNotFound(), "nonexistent")

