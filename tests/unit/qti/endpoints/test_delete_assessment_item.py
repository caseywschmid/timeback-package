"""Unit tests for delete_assessment_item endpoint.

Tests the delete_assessment_item function that permanently deletes a QTI assessment item.
"""

from typing import Any, Dict, Optional
import pytest

from timeback.services.qti.endpoints.delete_assessment_item import delete_assessment_item


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self, response_data: Optional[Dict[str, Any]] = None):
        """Initialize with the response data to return."""
        self.response_data = response_data
        self.last_path: str = ""
        self.delete_called: bool = False

    def delete(self, path: str) -> Optional[Dict[str, Any]]:
        """Mock DELETE request."""
        self.last_path = path
        self.delete_called = True
        return self.response_data


class TestDeleteAssessmentItem:
    """Tests for delete_assessment_item endpoint."""

    def test_delete_assessment_item_success(self) -> None:
        """Test successful deletion of an assessment item."""
        mock_http = MockHttpClient(None)  # DELETE typically returns None on success
        
        result = delete_assessment_item(mock_http, "item-001")
        
        assert result is None
        assert mock_http.delete_called
        assert mock_http.last_path == "/assessment-items/item-001"

    def test_delete_assessment_item_with_different_identifier(self) -> None:
        """Test that the identifier is correctly placed in the path."""
        mock_http = MockHttpClient(None)
        
        result = delete_assessment_item(mock_http, "math-question-42")
        
        assert mock_http.last_path == "/assessment-items/math-question-42"

    def test_delete_assessment_item_returns_response_if_present(self) -> None:
        """Test that response data is returned if provided."""
        response_data = {"message": "Item deleted successfully"}
        mock_http = MockHttpClient(response_data)
        
        result = delete_assessment_item(mock_http, "item-001")
        
        assert result == response_data

    def test_delete_assessment_item_path_format(self) -> None:
        """Test that the path is correctly formatted for various identifiers."""
        test_cases = [
            "simple-id",
            "item-with-numbers-123",
            "UPPERCASE-ID",
            "mixed_Case-With_underscores"
        ]
        
        for identifier in test_cases:
            mock_http = MockHttpClient(None)
            delete_assessment_item(mock_http, identifier)
            assert mock_http.last_path == f"/assessment-items/{identifier}"

