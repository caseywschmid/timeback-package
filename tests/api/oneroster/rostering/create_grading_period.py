"""API test for create_grading_period endpoint."""

from timeback import Timeback
from timeback.models.request import TimebackCreateGradingPeriodRequest
from timeback.models.timeback_academic_session import TimebackAcademicSession
from timeback.enums import TimebackAcademicSessionType
from timeback.models.timeback_org_ref import TimebackOrgRef


def test_create_grading_period():
    """Test creating a grading period."""
    client = Timeback()
    session = TimebackAcademicSession(
        title="Test Q1 2024",
        type=TimebackAcademicSessionType.GRADING_PERIOD,
        startDate="2024-08-01",
        endDate="2024-10-15",
        schoolYear=2024,
        org=TimebackOrgRef(sourcedId="YOUR_SCHOOL_SOURCED_ID"),  # Replace with actual school ID
    )
    request = TimebackCreateGradingPeriodRequest(academic_session=session)
    response = client.oneroster.rostering.create_grading_period(request)
    print(f"Created grading period: {response.sourcedIdPairs.allocatedSourcedId}")


if __name__ == "__main__":
    test_create_grading_period()

