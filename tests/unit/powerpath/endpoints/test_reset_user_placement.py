"""Unit tests for reset_user_placement endpoint."""

import pytest

from timeback.services.powerpath.endpoints.reset_user_placement import reset_user_placement
from timeback.models.response import TimebackResetUserPlacementResponse
from timeback.models.request import TimebackResetUserPlacementRequest
from timeback.enums import TimebackSubject


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def post(self, path, json=None):
        self.last_path = path
        self.last_json = json
        return self.response_data


def test_reset_user_placement_success():
    """Test successful reset of user placement."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "placementResultsDeleted": 5,
            "onboardingReset": True,
        }
    )

    request = TimebackResetUserPlacementRequest(
        student="student-123",
        subject=TimebackSubject.MATH,
    )
    resp = reset_user_placement(mock_http, request)

    assert isinstance(resp, TimebackResetUserPlacementResponse)
    assert resp.success is True
    assert resp.placementResultsDeleted == 5
    assert resp.onboardingReset is True


def test_reset_user_placement_path_and_body():
    """Test that the correct path and body are sent."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "placementResultsDeleted": 3,
            "onboardingReset": True,
        }
    )

    request = TimebackResetUserPlacementRequest(
        student="student-456",
        subject=TimebackSubject.READING,
    )
    resp = reset_user_placement(mock_http, request)

    assert mock_http.last_path == "/powerpath/placement/resetUserPlacement"
    assert mock_http.last_json == {
        "student": "student-456",
        "subject": "Reading",
    }


def test_reset_user_placement_no_results_deleted():
    """Test when no placement results exist to delete."""
    mock_http = MockHttpClient(
        {
            "success": True,
            "placementResultsDeleted": 0,
            "onboardingReset": True,
        }
    )

    request = TimebackResetUserPlacementRequest(
        student="new-student",
        subject=TimebackSubject.SCIENCE,
    )
    resp = reset_user_placement(mock_http, request)

    assert isinstance(resp, TimebackResetUserPlacementResponse)
    assert resp.success is True
    assert resp.placementResultsDeleted == 0


def test_reset_user_placement_all_subjects():
    """Test reset works for all subject types."""
    subjects_to_test = [
        (TimebackSubject.READING, "Reading"),
        (TimebackSubject.LANGUAGE, "Language"),
        (TimebackSubject.VOCABULARY, "Vocabulary"),
        (TimebackSubject.SOCIAL_STUDIES, "Social Studies"),
        (TimebackSubject.WRITING, "Writing"),
        (TimebackSubject.SCIENCE, "Science"),
        (TimebackSubject.FAST_MATH, "FastMath"),
        (TimebackSubject.MATH, "Math"),
    ]

    for subject_enum, subject_value in subjects_to_test:
        mock_http = MockHttpClient(
            {
                "success": True,
                "placementResultsDeleted": 1,
                "onboardingReset": True,
            }
        )

        request = TimebackResetUserPlacementRequest(
            student="student-test",
            subject=subject_enum,
        )
        resp = reset_user_placement(mock_http, request)

        assert mock_http.last_json["subject"] == subject_value
        assert isinstance(resp, TimebackResetUserPlacementResponse)

