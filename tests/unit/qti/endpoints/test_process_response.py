"""Unit tests for process_response endpoint.

Tests the process_response function that validates and scores a candidate's response.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.process_response import process_response
from timeback.models.request import TimebackProcessResponseRequest
from timeback.models.response import TimebackProcessResponseResponse


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Dict[str, Any]):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.last_body: Dict[str, Any] = {}

    def post(self, path: str, json: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mock POST request."""
        self.last_path = path
        self.last_body = json or {}
        return self.response_data


def create_correct_response() -> Dict[str, Any]:
    """Create a mock correct response."""
    return {
        "score": 1.0,
        "feedback": {
            "identifier": "correct",
            "value": "Correct! Well done."
        }
    }


def create_incorrect_response() -> Dict[str, Any]:
    """Create a mock incorrect response."""
    return {
        "score": 0.0,
        "feedback": {
            "identifier": "incorrect",
            "value": "Incorrect. The correct answer is B."
        }
    }


def create_partial_response(score: float) -> Dict[str, Any]:
    """Create a mock partial credit response."""
    return {
        "score": score,
        "feedback": {
            "identifier": "partial",
            "value": f"You scored {score * 100}%."
        }
    }


class TestProcessResponse:
    """Tests for process_response endpoint."""

    def test_process_response_correct(self) -> None:
        """Test processing a correct response."""
        mock_data = create_correct_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="B"
        )
        result = process_response(mock_http, "item-001", request)
        
        assert isinstance(result, TimebackProcessResponseResponse)
        assert result.score == 1.0
        assert result.feedback.identifier == "correct"
        assert "Correct" in result.feedback.value
        assert mock_http.last_path == "/assessment-items/item-001/process-response"

    def test_process_response_incorrect(self) -> None:
        """Test processing an incorrect response."""
        mock_data = create_incorrect_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="A"
        )
        result = process_response(mock_http, "item-001", request)
        
        assert result.score == 0.0
        assert result.feedback.identifier == "incorrect"
        assert "Incorrect" in result.feedback.value

    def test_process_response_with_list_response(self) -> None:
        """Test processing a multi-value response."""
        mock_data = create_correct_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response=["A", "C"]
        )
        result = process_response(mock_http, "item-001", request)
        
        assert mock_http.last_body["response"] == ["A", "C"]

    def test_process_response_partial_credit(self) -> None:
        """Test processing a partial credit response."""
        mock_data = create_partial_response(0.75)
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="extended text response here"
        )
        result = process_response(mock_http, "item-001", request)
        
        assert result.score == 0.75
        assert result.feedback.identifier == "partial"

    def test_process_response_path_format(self) -> None:
        """Test that the path is correctly formatted."""
        mock_data = create_correct_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="math-q-42",
            response="B"
        )
        process_response(mock_http, "math-q-42", request)
        
        assert mock_http.last_path == "/assessment-items/math-q-42/process-response"

    def test_process_response_body_contains_identifier(self) -> None:
        """Test that the request body contains the identifier."""
        mock_data = create_correct_response()
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="B"
        )
        process_response(mock_http, "item-001", request)
        
        assert mock_http.last_body["identifier"] == "item-001"
        assert mock_http.last_body["response"] == "B"

    def test_process_response_feedback_structure(self) -> None:
        """Test that feedback structure is correctly parsed."""
        mock_data = {
            "score": 1.0,
            "feedback": {
                "identifier": "custom-feedback",
                "value": "Custom feedback message with details."
            }
        }
        mock_http = MockHttpClient(mock_data)
        
        request = TimebackProcessResponseRequest(
            identifier="item-001",
            response="B"
        )
        result = process_response(mock_http, "item-001", request)
        
        assert result.feedback.identifier == "custom-feedback"
        assert result.feedback.value == "Custom feedback message with details."

