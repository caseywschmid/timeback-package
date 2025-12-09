from timeback.services.oneroster.gradebook.endpoints.get_categories_for_class import (
    get_categories_for_class,
)
from timeback.models.request import (
    TimebackGetCategoriesForClassRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllCategoriesResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert path.endswith("/categories")
        # Simulate 200 response body
        return {
            "categories": [
                {
                    "sourcedId": "category-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "title": "Homework",
                    "weight": 0.3,
                },
                {
                    "sourcedId": "category-2",
                    "status": "active",
                    "dateLastModified": "2024-01-02T00:00:00Z",
                    "title": "Exams",
                    "weight": 0.7,
                }
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_categories_for_class_success():
    """Test successful retrieval of categories for a class."""
    request = TimebackGetCategoriesForClassRequest(
        class_sourced_id="class-123"
    )
    resp = get_categories_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllCategoriesResponse)
    assert len(resp.categories) == 2
    assert resp.categories[0].sourcedId == "category-1"
    assert resp.categories[0].status == TimebackStatus.ACTIVE
    assert resp.categories[0].title == "Homework"
    assert resp.categories[0].weight == 0.3
    assert resp.categories[1].sourcedId == "category-2"
    assert resp.categories[1].title == "Exams"
    assert resp.categories[1].weight == 0.7
    assert resp.total_count == 2
    assert resp.limit == 100


def test_get_categories_for_class_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,title")
    request = TimebackGetCategoriesForClassRequest(
        class_sourced_id="class-123",
        query_params=query_params
    )
    resp = get_categories_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetAllCategoriesResponse)
    assert len(resp.categories) == 2

