from timeback.services.oneroster.gradebook.endpoints.put_category import (
    put_category,
)
from timeback.models.request import TimebackPutCategoryRequest
from timeback.models.response import TimebackPutCategoryResponse
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def put(self, path, json=None):
        self.last_path = path
        self.last_json = json
        # Simulate 201 response body
        return {
            "category": {
                "sourcedId": "category-123",
                "status": "active",
                "dateLastModified": "2024-01-01T00:00:00Z",
                "title": "Updated Homework",
                "weight": 0.35,
            }
        }


def test_put_category_success():
    """Test successful category update."""
    mock_http = MockHttp()
    category = TimebackCategory(
        sourcedId="category-123",
        status=TimebackStatus.ACTIVE,
        title="Updated Homework",
        weight=0.35,
    )
    request = TimebackPutCategoryRequest(
        sourced_id="category-123",
        category=category
    )
    resp = put_category(mock_http, request)
    
    assert isinstance(resp, TimebackPutCategoryResponse)
    assert resp.category.sourcedId == "category-123"
    assert resp.category.title == "Updated Homework"
    assert resp.category.weight == 0.35
    # Verify correct path was called
    assert "/ims/oneroster/gradebook/v1p2/categories/category-123" in mock_http.last_path
    # Verify sourced_id is not in the body
    assert "sourced_id" not in mock_http.last_json
    assert "category" in mock_http.last_json


def test_put_category_with_metadata():
    """Test category update with metadata."""
    mock_http = MockHttp()
    category = TimebackCategory(
        sourcedId="category-456",
        status=TimebackStatus.ACTIVE,
        title="Projects",
        weight=0.25,
        metadata={"customField": "customValue"},
    )
    request = TimebackPutCategoryRequest(
        sourced_id="category-456",
        category=category
    )
    resp = put_category(mock_http, request)
    
    assert isinstance(resp, TimebackPutCategoryResponse)
    # Verify metadata is included in the body
    assert mock_http.last_json["category"].get("metadata") == {"customField": "customValue"}


def test_put_category_minimal_fields():
    """Test category update with minimal required fields."""
    class MockHttpMinimal:
        def put(self, path, json=None):
            return {
                "category": {
                    "sourcedId": "category-789",
                    "status": "active",
                    "title": "Quizzes",
                }
            }
    
    category = TimebackCategory(
        status=TimebackStatus.ACTIVE,
        title="Quizzes",
    )
    request = TimebackPutCategoryRequest(
        sourced_id="category-789",
        category=category
    )
    resp = put_category(MockHttpMinimal(), request)
    
    assert isinstance(resp, TimebackPutCategoryResponse)
    assert resp.category.title == "Quizzes"
    assert resp.category.weight is None  # Optional field not provided

