from timeback.services.oneroster.rostering.endpoints.create_course import create_course
from timeback.models.request import TimebackCreateCourseRequest, TimebackCreateCourseBody
from timeback.models.response import TimebackCreateCourseResponse


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["course"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_course_success():
    mock_http = MockHttp()
    body = TimebackCreateCourseBody(sourcedId="new-course", title="Math 101", orgSourcedId="org-001")
    request = TimebackCreateCourseRequest(course=body)
    resp = create_course(mock_http, request)
    assert isinstance(resp, TimebackCreateCourseResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-course"

