"""Unit tests for update_student_question_response endpoint."""

import pytest

from timeback.services.powerpath.endpoints.update_student_question_response import (
    update_student_question_response,
)
from timeback.models.request import TimebackUpdateStudentQuestionResponseRequest
from timeback.models.response import TimebackUpdateStudentQuestionResponseResponse


class MockHttp:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: dict):
        self.response_data = response_data
        self.last_path = None
        self.last_json = None

    def put(self, path: str, json: dict = None):
        self.last_path = path
        self.last_json = json
        return self.response_data


class TestUpdateStudentQuestionResponse:
    """Tests for update_student_question_response endpoint."""

    def test_update_response_powerpath100_success(self):
        """Test successful update for PowerPath-100 lesson."""
        mock_response = {
            "lessonType": "powerpath-100",
            "powerpathScore": 85.5,
            "responseResult": {
                "isCorrect": True,
                "score": 1,
                "feedback": "Correct!",
            },
            "accuracy": 0.9,
            "correctQuestions": 9,
            "totalQuestions": 10,
            "xp": 150,
            "multiplier": 1.5,
        }

        mock_http = MockHttp(mock_response)
        request = TimebackUpdateStudentQuestionResponseRequest(
            student="student-123",
            question="q-456",
            lesson="lesson-789",
            responses={"RESPONSE": "choice-A"},
        )
        resp = update_student_question_response(mock_http, request)

        assert isinstance(resp, TimebackUpdateStudentQuestionResponseResponse)
        assert resp.lessonType == "powerpath-100"
        assert resp.powerpathScore == 85.5
        assert resp.responseResult.isCorrect is True
        assert resp.responseResult.score == 1
        assert resp.accuracy == 0.9
        assert resp.xp == 150

    def test_update_response_quiz_success(self):
        """Test successful update for quiz lesson."""
        mock_response = {
            "lessonType": "quiz",
            "questionResult": {"some": "debug info"},
        }

        mock_http = MockHttp(mock_response)
        request = TimebackUpdateStudentQuestionResponseRequest(
            student="student-123",
            question="q-456",
            lesson="lesson-789",
            responses={"RESPONSE": "choice-B"},
        )
        resp = update_student_question_response(mock_http, request)

        assert resp.lessonType == "quiz"
        assert resp.questionResult is not None

    def test_update_response_correct_path_and_body(self):
        """Test correct path and request body."""
        mock_http = MockHttp({"lessonType": "quiz"})
        request = TimebackUpdateStudentQuestionResponseRequest(
            student="student-abc",
            question="q-xyz",
            lesson="lesson-123",
            responses={"RESPONSE": ["A", "B"]},
        )
        update_student_question_response(mock_http, request)

        assert mock_http.last_path == "/powerpath/updateStudentQuestionResponse"
        assert mock_http.last_json == {
            "student": "student-abc",
            "question": "q-xyz",
            "lesson": "lesson-123",
            "responses": {"RESPONSE": ["A", "B"]},
        }

    def test_update_response_with_deprecated_response_field(self):
        """Test using deprecated 'response' field."""
        mock_http = MockHttp({"lessonType": "test-out"})
        request = TimebackUpdateStudentQuestionResponseRequest(
            student="student-123",
            question="q-456",
            lesson="lesson-789",
            response="single-answer",
        )
        update_student_question_response(mock_http, request)

        assert mock_http.last_json["response"] == "single-answer"

    def test_update_response_all_lesson_types(self):
        """Test all valid lesson types."""
        lesson_types = ["powerpath-100", "quiz", "test-out", "placement", "unit-test"]

        for lesson_type in lesson_types:
            mock_response = {"lessonType": lesson_type}

            mock_http = MockHttp(mock_response)
            request = TimebackUpdateStudentQuestionResponseRequest(
                student="student-123",
                question="q-456",
                lesson="lesson-789",
                responses={"RESPONSE": "A"},
            )
            resp = update_student_question_response(mock_http, request)
            assert resp.lessonType == lesson_type

    def test_update_response_incorrect_answer(self):
        """Test handling incorrect answer."""
        mock_response = {
            "lessonType": "powerpath-100",
            "powerpathScore": 50.0,
            "responseResult": {
                "isCorrect": False,
                "score": 0,
                "feedback": "Try again!",
            },
            "accuracy": 0.5,
            "correctQuestions": 5,
            "totalQuestions": 10,
            "xp": 0,
            "multiplier": 1.0,
        }

        mock_http = MockHttp(mock_response)
        request = TimebackUpdateStudentQuestionResponseRequest(
            student="student-123",
            question="q-456",
            lesson="lesson-789",
            responses={"RESPONSE": "wrong-choice"},
        )
        resp = update_student_question_response(mock_http, request)

        assert resp.responseResult.isCorrect is False
        assert resp.responseResult.score == 0
        assert resp.xp == 0

