from timeback.services.oneroster.gradebook.endpoints.patch_assessment_line_item import (
    patch_assessment_line_item,
)
from timeback.models.request import TimebackPatchAssessmentLineItemRequest, TimebackPatchAssessmentLineItemBody
from timeback.models.response import TimebackPatchAssessmentLineItemResponse


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def patch(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "assessmentLineItem": {
                "sourcedId": "ali-001",
                "status": "active",
                "title": "Patched Title",
                "class": {"sourcedId": "class-001"},
                "school": {"sourcedId": "school-001"},
                "category": {"sourcedId": "cat-001"},
                "assignDate": "2024-01-01",
                "dueDate": "2024-01-15",
            }
        }


def test_patch_assessment_line_item_title_only():
    """Test partial update of just the title."""
    mock_http = MockHttp()
    body = TimebackPatchAssessmentLineItemBody(title="Patched Title")
    request = TimebackPatchAssessmentLineItemRequest(sourced_id="ali-001", assessmentLineItem=body)
    resp = patch_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackPatchAssessmentLineItemResponse)
    assert resp.assessmentLineItem.title == "Patched Title"
    assert mock_http.last_json["assessmentLineItem"]["title"] == "Patched Title"
    assert "dueDate" not in mock_http.last_json["assessmentLineItem"]


def test_patch_assessment_line_item_multiple_fields():
    """Test partial update of multiple fields."""
    mock_http = MockHttp()
    body = TimebackPatchAssessmentLineItemBody(
        title="Patched Title",
        description="Updated description",
        resultValueMax=150.0,
    )
    request = TimebackPatchAssessmentLineItemRequest(sourced_id="ali-001", assessmentLineItem=body)
    resp = patch_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackPatchAssessmentLineItemResponse)
    assert mock_http.last_json["assessmentLineItem"]["description"] == "Updated description"
    assert mock_http.last_json["assessmentLineItem"]["resultValueMax"] == 150.0

