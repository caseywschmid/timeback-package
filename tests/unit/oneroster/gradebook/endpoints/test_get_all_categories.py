from timeback.services.oneroster.gradebook.endpoints.get_all_categories import (
    get_all_categories,
)
from timeback.models.request import (
    TimebackGetAllCategoriesRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllCategoriesResponse
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


def test_get_all_categories_success():
    """Test successful retrieval of all categories."""
    mock_http = MockHttp()
    request = TimebackGetAllCategoriesRequest()
    resp = get_all_categories(mock_http, request)
    
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
    # Verify correct path was called
    assert mock_http.last_path == "/ims/oneroster/gradebook/v1p2/categories"


def test_get_all_categories_with_query_params():
    """Test retrieval with query parameters."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(
        limit=50,
        offset=10,
        fields=["sourcedId", "title"],
        sort="title",
        order_by="asc",
        filter="status='active'",
    )
    request = TimebackGetAllCategoriesRequest(query_params=query_params)
    resp = get_all_categories(mock_http, request)
    
    assert isinstance(resp, TimebackGetAllCategoriesResponse)
    assert len(resp.categories) == 2
    assert mock_http.last_params == {
        "limit": 50,
        "offset": 10,
        "fields": "sourcedId,title",
        "sort": "title",
        "orderBy": "asc",
        "filter": "status='active'",
    }


def test_get_all_categories_empty_list():
    """Test retrieval when no categories exist."""
    class MockHttpEmpty:
        def get(self, path, params=None):
            return {
                "categories": [],
                "totalCount": 0,
                "pageCount": 0,
                "pageNumber": 1,
                "offset": 0,
                "limit": 100,
            }
    
    request = TimebackGetAllCategoriesRequest()
    resp = get_all_categories(MockHttpEmpty(), request)
    
    assert isinstance(resp, TimebackGetAllCategoriesResponse)
    assert len(resp.categories) == 0
    assert resp.total_count == 0

