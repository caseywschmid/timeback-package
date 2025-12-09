from timeback.services.oneroster.rostering.endpoints.create_course_component import create_course_component
from timeback.models.request import TimebackCreateCourseComponentRequest, TimebackCreateCourseComponentBody
from timeback.models.response import TimebackCreateCourseComponentResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference


class MockHttp:
    def __init__(self):
        self.last_json = None

    def post(self, path, json=None):
        self.last_json = json
        return {"sourcedIdPairs": {"suppliedSourcedId": json["courseComponent"]["sourcedId"], "allocatedSourcedId": "alloc-001"}}


def test_create_course_component_success():
    mock_http = MockHttp()
    body = TimebackCreateCourseComponentBody(
        sourcedId="new-cc",
        title="Unit 1",
        course=TimebackSourcedIdReference(sourcedId="course-001"),
    )
    request = TimebackCreateCourseComponentRequest(courseComponent=body)
    resp = create_course_component(mock_http, request)
    assert isinstance(resp, TimebackCreateCourseComponentResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "new-cc"

