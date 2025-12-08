from timeback.services.oneroster.rostering.endpoints.add_student_to_class import add_student_to_class
from timeback.models.request import TimebackAddStudentToClassRequest
from timeback.models.response import TimebackAddStudentToClassResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["student"]["sourcedId"], "allocatedSourcedId": "enrollment-001"}}


def test_add_student_to_class_success():
    mock_http = MockHttp()
    request = TimebackAddStudentToClassRequest(class_sourced_id="class-001", student=TimebackSourcedIdReference(sourcedId="student-001"))
    resp = add_student_to_class(mock_http, request)
    assert isinstance(resp, TimebackAddStudentToClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "student-001"

