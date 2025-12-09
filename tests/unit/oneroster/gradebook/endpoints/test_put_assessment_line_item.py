from timeback.services.oneroster.gradebook.endpoints.put_assessment_line_item import (
    put_assessment_line_item,
)
from timeback.models.request import TimebackPutAssessmentLineItemRequest, TimebackPutAssessmentLineItemBody
from timeback.models.response import TimebackPutAssessmentLineItemResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def put(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "assessmentLineItem": {
                "sourcedId": "ali-001",
                "status": "active",
                "title": "Updated Quiz",
                "class": {"sourcedId": "class-001"},
                "school": {"sourcedId": "school-001"},
                "category": {"sourcedId": "cat-001"},
                "assignDate": "2024-01-01",
                "dueDate": "2024-01-20",
            }
        }


def test_put_assessment_line_item_success():
    """Test successful update."""
    mock_http = MockHttp()
    body = TimebackPutAssessmentLineItemBody(
        sourcedId="ali-001",
        title="Updated Quiz",
        assignDate="2024-01-01",
        dueDate="2024-01-20",
        class_=TimebackSourcedIdReference(sourcedId="class-001"),
        school=TimebackSourcedIdReference(sourcedId="school-001"),
        category=TimebackSourcedIdReference(sourcedId="cat-001"),
    )
    request = TimebackPutAssessmentLineItemRequest(sourced_id="ali-001", assessmentLineItem=body)
    resp = put_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackPutAssessmentLineItemResponse)
    assert resp.assessmentLineItem.title == "Updated Quiz"
    assert "/ims/oneroster/gradebook/v1p2/assessmentLineItems/ali-001" in mock_http.last_path
    assert "sourced_id" not in mock_http.last_json

