from timeback.services.oneroster.rostering.endpoints.add_teacher_to_class import add_teacher_to_class
from timeback.models.request import TimebackAddTeacherToClassRequest
from timeback.models.response import TimebackAddTeacherToClassResponse
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
                "suppliedSourcedId": json["teacher"]["sourcedId"],
                "allocatedSourcedId": "enrollment-001",
            }
        }


def test_add_teacher_to_class_success():
    """Test successful addition of teacher to class."""
    mock_http = MockHttp()
    request = TimebackAddTeacherToClassRequest(
        class_sourced_id="class-001",
        teacher=TimebackSourcedIdReference(sourcedId="teacher-001")
    )
    resp = add_teacher_to_class(mock_http, request)

    assert isinstance(resp, TimebackAddTeacherToClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "teacher-001"
    assert "/ims/oneroster/rostering/v1p2/classes/class-001/teachers" in mock_http.last_path

