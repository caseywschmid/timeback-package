from timeback.services.oneroster.gradebook.endpoints.get_score_scale import (
    get_score_scale,
)
from timeback.models.request import (
    TimebackGetScoreScaleRequest,
    TimebackQueryParams,
)
from timeback.models.response import TimebackGetScoreScaleResponse


class MockHttp:
    def get(self, path, params=None):
        assert path == "/ims/oneroster/gradebook/v1p2/scoreScales/scale-123"
        # Simulate 200 response body
        return {
            "scoreScale": {
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
        }


def test_get_score_scale_success():
    request = TimebackGetScoreScaleRequest(sourced_id="scale-123")
    resp = get_score_scale(MockHttp(), request)
    assert isinstance(resp, TimebackGetScoreScaleResponse)
    assert resp.score_scale.sourcedId == "scale-123"
    assert resp.score_scale.title == "Letter Grade Scale"
    assert len(resp.score_scale.scoreScaleValue) == 1


def test_get_score_scale_with_fields():
    query_params = TimebackQueryParams(fields="sourcedId,title")
    request = TimebackGetScoreScaleRequest(
        sourced_id="scale-123", query_params=query_params
    )
    resp = get_score_scale(MockHttp(), request)
    assert isinstance(resp, TimebackGetScoreScaleResponse)
    assert resp.score_scale.sourcedId == "scale-123"
