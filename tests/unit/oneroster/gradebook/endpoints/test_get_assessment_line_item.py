from timeback.services.oneroster.gradebook.endpoints.get_assessment_line_item import (
    get_assessment_line_item,
)
from timeback.models.request import TimebackGetAssessmentLineItemRequest, TimebackQueryParams
from timeback.models.response import TimebackGetAssessmentLineItemResponse


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_params = None

    def get(self, path, params=None):
        self.last_path = path
        self.last_params = params
        return {
            "assessmentLineItem": {
                "sourcedId": "ali-001",
                "status": "active",
                "title": "Quiz 1",
                "class": {"sourcedId": "class-001"},
                "school": {"sourcedId": "school-001"},
                "category": {"sourcedId": "cat-001"},
                "assignDate": "2024-01-01",
                "dueDate": "2024-01-15",
            }
        }


def test_get_assessment_line_item_success():
    """Test successful retrieval."""
    mock_http = MockHttp()
    request = TimebackGetAssessmentLineItemRequest(sourced_id="ali-001")
    resp = get_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackGetAssessmentLineItemResponse)
    assert resp.assessmentLineItem.sourcedId == "ali-001"
    assert resp.assessmentLineItem.title == "Quiz 1"
    assert "/ims/oneroster/gradebook/v1p2/assessmentLineItems/ali-001" in mock_http.last_path


def test_get_assessment_line_item_with_fields():
    """Test retrieval with fields parameter."""
    mock_http = MockHttp()
    query_params = TimebackQueryParams(fields=["sourcedId", "title"])
    request = TimebackGetAssessmentLineItemRequest(sourced_id="ali-002", query_params=query_params)
    resp = get_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackGetAssessmentLineItemResponse)
    assert mock_http.last_params == {"fields": "sourcedId,title"}

