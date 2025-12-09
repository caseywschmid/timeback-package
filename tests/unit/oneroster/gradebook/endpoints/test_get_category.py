from timeback.services.oneroster.gradebook.endpoints.get_category import (
    get_category,
)
from timeback.models.request import (
    TimebackGetCategoryRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetCategoryResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        # Simulate 200 response body
        return {
            "category": {
                "sourcedId": "category-123",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "title": "Homework",
                "weight": 0.3,
            }
        }


def test_get_category_success():
    """Test successful category retrieval."""
    mock_http = MockHttp()
    request = TimebackGetCategoryRequest(sourced_id="category-123")
    resp = get_category(mock_http, request)
    
    assert isinstance(resp, TimebackGetCategoryResponse)
    assert resp.category.sourcedId == "category-123"
    assert resp.category.status == TimebackStatus.ACTIVE
    assert resp.category.title == "Homework"
    assert resp.category.weight == 0.3
    # Verify correct path was called
    assert "/ims/oneroster/gradebook/v1p2/categories/category-123" in mock_http.last_path


def test_get_category_with_fields_param():
    """Test category retrieval with fields parameter."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(fields=["sourcedId", "title", "weight"])
    request = TimebackGetCategoryRequest(
        sourced_id="category-456",
        query_params=query_params
    )
    resp = get_category(mock_http, request)
    
    assert isinstance(resp, TimebackGetCategoryResponse)
    assert "/ims/oneroster/gradebook/v1p2/categories/category-456" in mock_http.last_path
    assert mock_http.last_params == {"fields": "sourcedId,title,weight"}


def test_get_category_minimal_response():
    """Test category retrieval with minimal response fields."""
    class MockHttpMinimal:
        def get(self, path, params=None):
            return {
                "category": {
                    "sourcedId": "category-789",
                    "status": "active",
                    "title": "Exams",
                }
            }
    
    request = TimebackGetCategoryRequest(sourced_id="category-789")
    resp = get_category(MockHttpMinimal(), request)
    
    assert isinstance(resp, TimebackGetCategoryResponse)
    assert resp.category.sourcedId == "category-789"
    assert resp.category.title == "Exams"
    assert resp.category.weight is None  # Optional field not provided

