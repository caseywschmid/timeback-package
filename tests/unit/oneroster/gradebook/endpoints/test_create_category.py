from timeback.services.oneroster.gradebook.endpoints.create_category import (
    create_category,
)
from timeback.models.request import TimebackCreateCategoryRequest
from timeback.models.response import TimebackCreateCategoryResponse
from timeback.models.timeback_category import TimebackCategory
from timeback.enums import TimebackStatus


class MockHttp:
    def __init__(self):
        self.last_body = None

    def post(self, path, json=None):
        assert path == "/ims/oneroster/gradebook/v1p2/categories"
        assert json is not None
        assert "category" in json
        self.last_body = json
        # Simulate 201 response body
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["category"].get("sourcedId", "generated-id"),
                "allocatedSourcedId": "allocated-category-456",
            }
        }


def test_create_category_success():
    """Test successful category creation."""
    mock_http = MockHttp()
    
    category = TimebackCategory(
        sourcedId="category-123",
        status=TimebackStatus.ACTIVE,
        title="Homework",
        weight=0.3,
    )

    request = TimebackCreateCategoryRequest(category=category)
    resp = create_category(mock_http, request)
    
    assert isinstance(resp, TimebackCreateCategoryResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "category-123"
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-category-456"
    # Verify request body structure
    assert mock_http.last_body["category"]["title"] == "Homework"
    assert mock_http.last_body["category"]["weight"] == 0.3


def test_create_category_minimal():
    """Test category creation with only required fields."""
    mock_http = MockHttp()
    
    # Only title and status are required
    category = TimebackCategory(
        status=TimebackStatus.ACTIVE,
        title="Exams",
    )

    request = TimebackCreateCategoryRequest(category=category)
    resp = create_category(mock_http, request)
    
    assert isinstance(resp, TimebackCreateCategoryResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-category-456"
    assert mock_http.last_body["category"]["title"] == "Exams"
    # Weight should not be in body since it's None and we use exclude_none
    assert "weight" not in mock_http.last_body["category"] or mock_http.last_body["category"]["weight"] is None


def test_create_category_with_metadata():
    """Test category creation with metadata."""
    mock_http = MockHttp()
    
    category = TimebackCategory(
        sourcedId="category-789",
        status=TimebackStatus.ACTIVE,
        title="Quizzes",
        weight=0.2,
        metadata={"customField": "customValue", "priority": 1},
    )

    request = TimebackCreateCategoryRequest(category=category)
    resp = create_category(mock_http, request)
    
    assert isinstance(resp, TimebackCreateCategoryResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "category-789"
    assert mock_http.last_body["category"]["metadata"] == {"customField": "customValue", "priority": 1}

