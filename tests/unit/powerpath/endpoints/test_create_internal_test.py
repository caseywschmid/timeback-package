"""Unit tests for create_internal_test endpoint."""

import pytest

from timeback.services.powerpath.endpoints.create_internal_test import create_internal_test
from timeback.models.response import TimebackCreateInternalTestResponse
from timeback.models.request import (
    TimebackCreateInternalQtiTestRequest,
    TimebackCreateInternalAssessmentBankTestRequest,
    TimebackQtiTestConfig,
    TimebackAssessmentBankConfig,
    TimebackAssessmentBankResource,
)


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


def test_create_internal_qti_test_success():
    """Test successful creation of internal QTI test."""
    mock_http = MockHttpClient(
        {
            "lessonType": "quiz",
            "testType": "qti",
            "lessonId": "lesson-123",
            "courseComponentId": "component-456",
            "resourceId": "resource-789",
        }
    )

    request = TimebackCreateInternalQtiTestRequest(
        courseId="course-123",
        lessonType="quiz",
        qti=TimebackQtiTestConfig(
            url="https://qti.example.com/test.xml",
            title="Chapter 1 Quiz",
        ),
    )
    resp = create_internal_test(mock_http, request)

    assert isinstance(resp, TimebackCreateInternalTestResponse)
    assert resp.lessonType == "quiz"
    assert resp.testType == "qti"
    assert resp.lessonId == "lesson-123"
    assert resp.courseComponentId == "component-456"
    assert resp.resourceId == "resource-789"


def test_create_internal_assessment_bank_test_success():
    """Test successful creation of internal assessment bank test."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "testType": "assessment-bank",
            "lessonId": "lesson-bank-123",
            "courseComponentId": "component-bank-456",
            "resourceId": "parent-resource-789",
            "childResourceIds": ["child-1", "child-2", "child-3"],
            "grades": ["5", "6"],
        }
    )

    request = TimebackCreateInternalAssessmentBankTestRequest(
        courseId="course-123",
        lessonType="placement",
        assessmentBank=TimebackAssessmentBankConfig(
            resources=[
                TimebackAssessmentBankResource(url="https://qti.example.com/test1.xml", title="Test 1"),
                TimebackAssessmentBankResource(url="https://qti.example.com/test2.xml", title="Test 2"),
                TimebackAssessmentBankResource(url="https://qti.example.com/test3.xml", title="Test 3"),
            ]
        ),
        grades=["5", "6"],
    )
    resp = create_internal_test(mock_http, request)

    assert isinstance(resp, TimebackCreateInternalTestResponse)
    assert resp.lessonType == "placement"
    assert resp.testType == "assessment-bank"
    assert resp.childResourceIds == ["child-1", "child-2", "child-3"]
    assert resp.grades == ["5", "6"]


def test_create_internal_qti_test_path_and_body():
    """Test that the correct path and body are sent for QTI test."""
    mock_http = MockHttpClient(
        {
            "lessonType": "unit-test",
            "testType": "qti",
            "lessonId": "lesson-id",
            "courseComponentId": "component-id",
            "resourceId": "resource-id",
        }
    )

    request = TimebackCreateInternalQtiTestRequest(
        courseId="course-456",
        lessonType="unit-test",
        lessonTitle="Unit 1 Test",
        qti=TimebackQtiTestConfig(
            url="https://qti.example.com/unit1.xml",
            title="Unit 1 Assessment",
            metadata={"difficulty": "medium"},
        ),
    )
    resp = create_internal_test(mock_http, request)

    assert mock_http.last_path == "/powerpath/createInternalTest"
    assert mock_http.last_json["courseId"] == "course-456"
    assert mock_http.last_json["lessonType"] == "unit-test"
    assert mock_http.last_json["testType"] == "qti"
    assert mock_http.last_json["qti"]["url"] == "https://qti.example.com/unit1.xml"
    assert mock_http.last_json["qti"]["title"] == "Unit 1 Assessment"
    assert mock_http.last_json["qti"]["metadata"]["difficulty"] == "medium"


def test_create_internal_test_for_test_out():
    """Test creating internal test for test-out with xp."""
    mock_http = MockHttpClient(
        {
            "lessonType": "test-out",
            "testType": "qti",
            "lessonId": "testout-lesson",
            "courseComponentId": "testout-component",
            "resourceId": "testout-resource",
        }
    )

    request = TimebackCreateInternalQtiTestRequest(
        courseId="course-789",
        lessonType="test-out",
        xp=100,
        qti=TimebackQtiTestConfig(url="https://qti.example.com/testout.xml"),
    )
    resp = create_internal_test(mock_http, request)

    assert isinstance(resp, TimebackCreateInternalTestResponse)
    assert resp.lessonType == "test-out"
    assert mock_http.last_json["xp"] == 100


def test_create_internal_placement_test_with_course_on_fail():
    """Test creating internal placement test with courseIdOnFail."""
    mock_http = MockHttpClient(
        {
            "lessonType": "placement",
            "testType": "qti",
            "lessonId": "placement-lesson",
            "courseComponentId": "placement-component",
            "resourceId": "placement-resource",
            "courseIdOnFail": "remedial-course",
            "grades": ["3", "4"],
        }
    )

    request = TimebackCreateInternalQtiTestRequest(
        courseId="advanced-course",
        lessonType="placement",
        grades=["3", "4"],
        courseIdOnFail="remedial-course",
        qti=TimebackQtiTestConfig(url="https://qti.example.com/placement.xml"),
    )
    resp = create_internal_test(mock_http, request)

    assert isinstance(resp, TimebackCreateInternalTestResponse)
    assert resp.courseIdOnFail == "remedial-course"
    assert resp.grades == ["3", "4"]
    assert mock_http.last_json["courseIdOnFail"] == "remedial-course"

