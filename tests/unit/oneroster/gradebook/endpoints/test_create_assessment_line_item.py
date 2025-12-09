from timeback.services.oneroster.gradebook.endpoints.create_assessment_line_item import (
    create_assessment_line_item,
)
from timeback.models.request import (
    TimebackCreateAssessmentLineItemRequest,
    TimebackCreateAssessmentLineItemBody,
)
from timeback.models.response import TimebackCreateAssessmentLineItemResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": json["assessmentLineItem"]["sourcedId"],
                "allocatedSourcedId": "allocated-ali-001",
            }
        }


def test_create_assessment_line_item_success():
    """Test successful assessment line item creation."""
    mock_http = MockHttp()
    body = TimebackCreateAssessmentLineItemBody(
        sourcedId="ali-001",
        title="Quiz 1",
        assignDate="2024-01-01",
        dueDate="2024-01-15",
        class_=TimebackSourcedIdReference(sourcedId="class-001"),
        school=TimebackSourcedIdReference(sourcedId="school-001"),
        category=TimebackSourcedIdReference(sourcedId="cat-001"),
    )
    request = TimebackCreateAssessmentLineItemRequest(assessmentLineItem=body)
    resp = create_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackCreateAssessmentLineItemResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "ali-001"
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-ali-001"
    assert "/ims/oneroster/gradebook/v1p2/assessmentLineItems" in mock_http.last_path


def test_create_assessment_line_item_with_optional_fields():
    """Test creation with optional fields."""
    mock_http = MockHttp()
    body = TimebackCreateAssessmentLineItemBody(
        sourcedId="ali-002",
        title="Homework 1",
        assignDate="2024-01-02",
        dueDate="2024-01-16",
        class_=TimebackSourcedIdReference(sourcedId="class-001"),
        school=TimebackSourcedIdReference(sourcedId="school-001"),
        category=TimebackSourcedIdReference(sourcedId="cat-002"),
        description="Chapter 5 problems",
        resultValueMin=0.0,
        resultValueMax=100.0,
    )
    request = TimebackCreateAssessmentLineItemRequest(assessmentLineItem=body)
    resp = create_assessment_line_item(mock_http, request)

    assert isinstance(resp, TimebackCreateAssessmentLineItemResponse)
    assert mock_http.last_json["assessmentLineItem"]["description"] == "Chapter 5 problems"

