"""Unit tests for get_all_questions endpoint.

Tests the get_all_questions function that retrieves all assessment items
referenced by an assessment test.
"""

from typing import Any, Dict, List
import pytest

from timeback.services.qti.endpoints.get_all_questions import get_all_questions
from timeback.models.response import TimebackGetAllQuestionsResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""

    def get(self, path: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock GET request."""
        self.last_path = path
        return self.response_data


def create_mock_question_data(
    identifier: str = "item-001",
    title: str = "Test Question",
    test_part: str = "part-1",
    section: str = "section-1"
) -> Dict[str, Any]:
    """Create mock question data for testing."""
    return {
        "reference": {
            "identifier": f"ref-{identifier}",
            "href": f"/assessment-items/{identifier}",
            "testPart": test_part,
            "section": section
        },
        "question": {
            "identifier": identifier,
            "title": title,
            "type": "choice",
            "qtiVersion": "3.0",
            "timeDependent": False,
            "adaptive": False,
            "responseDeclarations": [
                {
                    "identifier": "RESPONSE",
                    "cardinality": "single",
                    "baseType": "identifier",
                    "correctResponse": {"value": ["A"]}
                }
            ]
        }
    }


def create_mock_response(
    test_identifier: str = "test-001",
    test_title: str = "Test Assessment",
    questions: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a mock get_all_questions response."""
    if questions is None:
        questions = [create_mock_question_data()]
    
    return {
        "assessmentTest": test_identifier,
        "title": test_title,
        "totalQuestions": len(questions),
        "questions": questions
    }


class TestGetAllQuestions:
    """Tests for get_all_questions endpoint."""

    def test_get_all_questions_success(self) -> None:
        """Test successful retrieval of all questions."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        assert isinstance(result, TimebackGetAllQuestionsResponse)
        assert result.assessment_test == "test-001"
        assert result.title == "Test Assessment"
        assert result.total_questions == 1
        assert len(result.questions) == 1
        assert mock_http.last_path == "/assessment-tests/test-001/questions"

    def test_get_all_questions_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_data = create_mock_response(test_identifier="math-final-42")
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "math-final-42")
        
        assert result.assessment_test == "math-final-42"
        assert mock_http.last_path == "/assessment-tests/math-final-42/questions"

    def test_get_all_questions_multiple_questions(self) -> None:
        """Test response with multiple questions."""
        questions = [
            create_mock_question_data("item-001", "Question 1", "part-1", "section-1"),
            create_mock_question_data("item-002", "Question 2", "part-1", "section-2"),
            create_mock_question_data("item-003", "Question 3", "part-2", "section-1"),
        ]
        mock_data = create_mock_response(questions=questions)
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        assert result.total_questions == 3
        assert len(result.questions) == 3
        assert result.questions[0].question.identifier == "item-001"
        assert result.questions[1].question.identifier == "item-002"
        assert result.questions[2].question.identifier == "item-003"

    def test_get_all_questions_validates_reference(self) -> None:
        """Test that question references are correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        question = result.questions[0]
        assert question.reference.identifier == "ref-item-001"
        assert question.reference.href == "/assessment-items/item-001"
        assert question.reference.test_part == "part-1"
        assert question.reference.section == "section-1"

    def test_get_all_questions_validates_question_data(self) -> None:
        """Test that question data is correctly parsed."""
        mock_data = create_mock_response()
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        question_data = result.questions[0].question
        assert question_data.identifier == "item-001"
        assert question_data.title == "Test Question"
        assert question_data.type == "choice"
        assert question_data.qtiVersion == "3.0"

    def test_get_all_questions_empty_test(self) -> None:
        """Test response with no questions."""
        mock_data = create_mock_response(questions=[])
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        assert result.total_questions == 0
        assert len(result.questions) == 0

    def test_get_all_questions_multiple_test_parts(self) -> None:
        """Test response with questions from multiple test parts."""
        questions = [
            create_mock_question_data("item-001", "Q1", "part-1", "section-1"),
            create_mock_question_data("item-002", "Q2", "part-2", "section-1"),
        ]
        mock_data = create_mock_response(questions=questions)
        mock_http = MockHttpClient(mock_data)
        
        result = get_all_questions(mock_http, "test-001")
        
        assert result.questions[0].reference.test_part == "part-1"
        assert result.questions[1].reference.test_part == "part-2"

