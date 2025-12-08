"""API test for get_all_grading_periods endpoint."""

from timeback import Timeback
from timeback.models.request import TimebackGetAllGradingPeriodsRequest


def test_get_all_grading_periods():
    """Test fetching all grading periods."""
    client = Timeback()
    request = TimebackGetAllGradingPeriodsRequest()
    response = client.oneroster.rostering.get_all_grading_periods(request)
    print(f"Total grading periods: {response.total_count}")
    for gp in response.academicSessions[:5]:
        print(f"  - {gp.sourcedId}: {gp.title} ({gp.type.value})")


if __name__ == "__main__":
    test_get_all_grading_periods()

