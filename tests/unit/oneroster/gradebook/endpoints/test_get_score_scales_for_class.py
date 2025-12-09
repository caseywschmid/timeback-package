from timeback.services.oneroster.gradebook.endpoints.get_score_scales_for_class import (
    get_score_scales_for_class,
)
from timeback.models.request import (
    TimebackGetScoreScalesForClassRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetScoreScalesForSchoolResponse
from timeback.enums import TimebackStatus


class MockHttp:
    def get(self, path, params=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert path.endswith("/scoreScales")
        # Simulate 200 response body
        return {
            "scoreScales": [
                {
                    "sourcedId": "scale-1",
                    "status": "active",
                    "dateLastModified": "2024-01-01T00:00:00Z",
                    "metadata": {},
                    "title": "Letter Grade Scale",
                    "type": "letter",
                    "class": {"sourcedId": "class-123"},
                    "course": {"sourcedId": "course-456"},
                    "scoreScaleValue": [
                        {
                            "itemValueLHS": "90",
                            "itemValueRHS": "100",
                            "value": "A",
                            "description": "Excellent"
                        },
                        {
                            "itemValueLHS": "80",
                            "itemValueRHS": "89",
                            "value": "B",
                            "description": "Good"
                        }
                    ]
                },
                {
                    "sourcedId": "scale-2",
                    "status": "active",
                    "dateLastModified": "2024-01-02T00:00:00Z",
                    "title": "Percentage Scale",
                    "type": "percentage",
                    "class": {"sourcedId": "class-123"},
                    "scoreScaleValue": [
                        {
                            "itemValueLHS": "0",
                            "itemValueRHS": "100",
                            "value": "0-100"
                        }
                    ]
                }
            ],
            "totalCount": 2,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_score_scales_for_class_success():
    """Test successful retrieval of score scales for a class."""
    request = TimebackGetScoreScalesForClassRequest(
        class_sourced_id="class-123"
    )
    resp = get_score_scales_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetScoreScalesForSchoolResponse)
    assert len(resp.score_scales) == 2
    assert resp.score_scales[0].sourcedId == "scale-1"
    assert resp.score_scales[0].status == TimebackStatus.ACTIVE
    assert resp.score_scales[0].title == "Letter Grade Scale"
    assert resp.score_scales[0].type == "letter"
    assert resp.score_scales[0].class_.sourcedId == "class-123"
    assert resp.score_scales[0].course.sourcedId == "course-456"
    assert len(resp.score_scales[0].scoreScaleValue) == 2
    assert resp.score_scales[0].scoreScaleValue[0].value == "A"
    assert resp.score_scales[1].sourcedId == "scale-2"
    assert resp.score_scales[1].title == "Percentage Scale"
    assert resp.total_count == 2
    assert resp.limit == 100


def test_get_score_scales_for_class_with_query_params():
    """Test retrieval with query parameters."""
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,title")
    request = TimebackGetScoreScalesForClassRequest(
        class_sourced_id="class-123",
        query_params=query_params
    )
    resp = get_score_scales_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackGetScoreScalesForSchoolResponse)
    assert len(resp.score_scales) == 2

