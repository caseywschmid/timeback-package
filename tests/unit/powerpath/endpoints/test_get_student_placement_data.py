"""Unit tests for get_student_placement_data endpoint."""

import pytest

from timeback.services.powerpath.endpoints.get_student_placement_data import (
    get_student_placement_data,
)
from timeback.models import (
    TimebackSubjectPlacementData,
    TimebackPlacementTestStatus,
    TimebackPlacementTestSource,
)


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None

    def get(self, path, params=None):
        self.last_path = path
        return self.response_data


def test_get_student_placement_data_success():
    """Test successful retrieval of student placement data."""
    mock_http = MockHttpClient(
        {
            "Math": {
                "startingGrade": 3,
                "currentGrade": 5,
                "subjectLowestGrade": 1,
                "subjectHighestGrade": 8,
                "RIT": {
                    "GROWTH": {"score": 210, "grade": 5},
                    "SCREENING": {"score": 205, "grade": 4},
                },
                "results": [
                    {
                        "testId": "test-1",
                        "title": "Grade 3 Math Placement",
                        "subject": "Math",
                        "grade": 3,
                        "status": "PASSED",
                        "score": 92.5,
                        "completedAt": "2024-01-15T10:30:00Z",
                        "source": "PLACEMENT",
                        "masteryTrackProcessed": True,
                    },
                    {
                        "testId": "test-2",
                        "title": "Grade 4 Math Placement",
                        "subject": "Math",
                        "grade": 4,
                        "status": "PASSED",
                        "score": 88.0,
                        "completedAt": "2024-01-16T14:00:00Z",
                        "source": "EDULASTIC",
                    },
                ],
                "status": "in_progress",
                "nextTestId": "test-3",
            },
            "Reading": {
                "startingGrade": 4,
                "currentGrade": 4,
                "subjectLowestGrade": 1,
                "subjectHighestGrade": 8,
                "RIT": {
                    "GROWTH": {"score": 195, "grade": 4},
                },
                "results": [],
                "status": "not_started",
                "nextTestId": "reading-test-1",
            },
        }
    )

    resp = get_student_placement_data(mock_http, "student-123")

    assert len(resp) == 2
    assert "Math" in resp
    assert "Reading" in resp

    math_data = resp["Math"]
    assert isinstance(math_data, TimebackSubjectPlacementData)
    assert math_data.startingGrade == 3
    assert math_data.currentGrade == 5
    assert math_data.RIT.GROWTH.score == 210
    assert len(math_data.results) == 2
    assert math_data.results[0].status == TimebackPlacementTestStatus.PASSED
    assert math_data.results[0].source == TimebackPlacementTestSource.PLACEMENT
    assert math_data.nextTestId == "test-3"


def test_get_student_placement_data_path():
    """Test that the correct path is used."""
    mock_http = MockHttpClient(
        {
            "Math": {
                "startingGrade": 1,
                "currentGrade": 1,
                "subjectLowestGrade": 1,
                "subjectHighestGrade": 8,
                "RIT": {},
                "results": [],
                "status": "not_started",
                "nextTestId": None,
            }
        }
    )

    resp = get_student_placement_data(mock_http, "student-456")

    assert mock_http.last_path == "/powerpath/placement/student-456"


def test_get_student_placement_data_all_subjects():
    """Test response with all subjects."""
    all_subjects = ["Reading", "Language", "Vocabulary", "Social Studies", 
                    "Writing", "Science", "FastMath", "Math"]
    
    response_data = {}
    for subject in all_subjects:
        response_data[subject] = {
            "startingGrade": 3,
            "currentGrade": 3,
            "subjectLowestGrade": 1,
            "subjectHighestGrade": 8,
            "RIT": {},
            "results": [],
            "status": "not_started",
            "nextTestId": f"{subject.lower()}-test-1",
        }

    mock_http = MockHttpClient(response_data)
    resp = get_student_placement_data(mock_http, "student-all-subjects")

    assert len(resp) == 8
    for subject in all_subjects:
        assert subject in resp
        assert isinstance(resp[subject], TimebackSubjectPlacementData)


def test_get_student_placement_data_completed():
    """Test when placement is completed (nextTestId is null)."""
    mock_http = MockHttpClient(
        {
            "Math": {
                "startingGrade": 3,
                "currentGrade": 6,
                "subjectLowestGrade": 1,
                "subjectHighestGrade": 8,
                "RIT": {
                    "GROWTH": {"score": 220, "grade": 6},
                },
                "results": [
                    {
                        "testId": "test-final",
                        "title": "Grade 6 Math Placement",
                        "subject": "Math",
                        "grade": 6,
                        "status": "FAILED",
                        "score": 75.0,
                        "completedAt": "2024-02-01T09:00:00Z",
                        "source": "PLACEMENT",
                    }
                ],
                "status": "completed",
                "nextTestId": None,
            }
        }
    )

    resp = get_student_placement_data(mock_http, "completed-student")

    math_data = resp["Math"]
    assert math_data.status == "completed"
    assert math_data.nextTestId is None
    assert math_data.results[0].status == TimebackPlacementTestStatus.FAILED

