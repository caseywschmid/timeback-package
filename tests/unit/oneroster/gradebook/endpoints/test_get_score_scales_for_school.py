from timeback.services.oneroster.gradebook.endpoints.get_score_scales_for_school import (
    get_score_scales_for_school,
)
from timeback.models.request import (
    TimebackGetScoreScalesForSchoolRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetScoreScalesForSchoolResponse


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/schools/school-123/scoreScales"
        # Simulate 200 response body
        return {
            "scoreScales": [
                {
                    "sourcedId": "scale-123",
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


def test_get_score_scales_for_school_success():
    request = TimebackGetScoreScalesForSchoolRequest(sourced_id="school-123")
    resp = get_score_scales_for_school(MockHttp(), request)
    assert isinstance(resp, TimebackGetScoreScalesForSchoolResponse)
    assert len(resp.score_scales) == 1
    assert resp.score_scales[0].sourcedId == "scale-123"
    assert resp.total_count == 1


def test_get_score_scales_for_school_with_params():
    query_params = TimebackQueryParams(limit=10, offset=0)
    request = TimebackGetScoreScalesForSchoolRequest(
        sourced_id="school-123", query_params=query_params
    )
    resp = get_score_scales_for_school(MockHttp(), request)
    assert isinstance(resp, TimebackGetScoreScalesForSchoolResponse)
    assert resp.limit == 100  # Mock returns 100, but we verify the call succeeded
