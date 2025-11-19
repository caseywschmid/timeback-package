from timeback.services.oneroster.gradebook.endpoints.get_all_score_scales import (
    get_all_score_scales,
)
from timeback.models.request import (
    TimebackGetAllScoreScalesRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetAllScoreScalesResponse


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/scoreScales"
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
                    "course": None,
                    "scoreScaleValue": [
                        {
                            "itemValueLHS": "90",
                            "itemValueRHS": "100",
                            "value": "A",
                            "description": "Excellent",
                        }
                    ],
                }
            ],
            "totalCount": 1,
            "pageCount": 1,
            "pageNumber": 1,
            "offset": 0,
            "limit": 100,
        }


def test_get_all_score_scales_success():
    request = TimebackGetAllScoreScalesRequest()
    resp = get_all_score_scales(MockHttp(), request)
    assert isinstance(resp, TimebackGetAllScoreScalesResponse)
    assert len(resp.score_scales) == 1
    assert resp.score_scales[0].sourcedId == "scale-1"
    assert resp.score_scales[0].title == "Letter Grade Scale"
    assert resp.total_count == 1
    assert resp.limit == 100


def test_get_all_score_scales_with_query_params():
    query_params = TimebackQueryParams(limit=50, offset=10, fields="sourcedId,title")
    request = TimebackGetAllScoreScalesRequest(query_params=query_params)
    resp = get_all_score_scales(MockHttp(), request)
    assert isinstance(resp, TimebackGetAllScoreScalesResponse)
    assert len(resp.score_scales) == 1
