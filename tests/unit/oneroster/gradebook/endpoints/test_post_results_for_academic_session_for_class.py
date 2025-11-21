from timeback.services.oneroster.gradebook.endpoints.post_results_for_academic_session_for_class import (
    post_results_for_academic_session_for_class,
)
from timeback.models.request import (
    TimebackPostResultsForAcademicSessionForClassRequest,
    TimebackCreateResultBody,
)
from timeback.models.response import TimebackPostResultsForAcademicSessionForClassResponse
from timeback.models.timeback_sourced_id_ref import TimebackSourcedIdReference
from timeback.enums import TimebackStatus, TimebackScoreStatus


class MockHttp:
    def post(self, path, json=None):
        assert path.startswith("/ims/oneroster/gradebook/v1p2/classes/")
        assert "/academicSessions/" in path
        assert path.endswith("/results")
        assert json is not None
        assert "results" in json
        assert isinstance(json["results"], list)
        # Simulate 201 response body with sourcedIdPairs
        # Use the first result's sourcedId if available
        first_result_sourced_id = json["results"][0].get("sourcedId", "temp-id") if json["results"] else "temp-id"
        return {
            "sourcedIdPairs": {
                "suppliedSourcedId": first_result_sourced_id,
                "allocatedSourcedId": "allocated-result-123",
            }
        }


def test_post_results_for_academic_session_for_class_success():
    """Test successful result creation for an academic session and class."""
    class_sourced_id = "class-123"
    academic_session_sourced_id = "session-456"
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    request = TimebackPostResultsForAcademicSessionForClassRequest(
        class_sourced_id=class_sourced_id,
        academic_session_sourced_id=academic_session_sourced_id,
        results=[result1]
    )
    resp = post_results_for_academic_session_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostResultsForAcademicSessionForClassResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-result-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-1"


def test_post_results_for_academic_session_for_class_multiple_results():
    """Test creating multiple results for an academic session and class."""
    class_sourced_id = "class-456"
    academic_session_sourced_id = "session-789"
    result1 = TimebackCreateResultBody(
        sourcedId="result-1",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        score=95.5,
    )
    result2 = TimebackCreateResultBody(
        sourcedId="result-2",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-2"),
        scoreStatus=TimebackScoreStatus.SUBMITTED,
        scoreDate="2024-01-16T10:00:00Z",
        score=88.0,
    )
    request = TimebackPostResultsForAcademicSessionForClassRequest(
        class_sourced_id=class_sourced_id,
        academic_session_sourced_id=academic_session_sourced_id,
        results=[result1, result2]
    )
    resp = post_results_for_academic_session_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostResultsForAcademicSessionForClassResponse)
    assert resp.sourcedIdPairs.allocatedSourcedId == "allocated-result-123"
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-1"  # First result's sourcedId


def test_post_results_for_academic_session_for_class_with_all_fields():
    """Test result creation with all optional fields."""
    class_sourced_id = "class-789"
    academic_session_sourced_id = "session-012"
    result = TimebackCreateResultBody(
        sourcedId="result-full",
        lineItem=TimebackSourcedIdReference(sourcedId="line-item-1"),
        student=TimebackSourcedIdReference(sourcedId="student-1"),
        scoreStatus=TimebackScoreStatus.FULLY_GRADED,
        scoreDate="2024-01-15T10:00:00Z",
        status=TimebackStatus.ACTIVE,
        score=95.5,
        textScore="A",
        comment="Excellent work",
        class_=TimebackSourcedIdReference(sourcedId=class_sourced_id),
        scoreScale=TimebackSourcedIdReference(sourcedId="scale-1"),
    )
    request = TimebackPostResultsForAcademicSessionForClassRequest(
        class_sourced_id=class_sourced_id,
        academic_session_sourced_id=academic_session_sourced_id,
        results=[result]
    )
    resp = post_results_for_academic_session_for_class(MockHttp(), request)
    
    assert isinstance(resp, TimebackPostResultsForAcademicSessionForClassResponse)
    assert resp.sourcedIdPairs.suppliedSourcedId == "result-full"

