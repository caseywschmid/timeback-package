"""Unit tests for delete_stimulus endpoint.

Tests the delete_stimulus function that deletes a QTI stimulus.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.delete_stimulus import delete_stimulus


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self):
        """Initialize mock client."""
        self.last_path: str = ""
        self.delete_called: bool = False

    def delete(self, path: str) -> None:
        """Mock DELETE request."""
        self.last_path = path
        self.delete_called = True
        return None


class TestDeleteStimulus:
    """Tests for delete_stimulus endpoint."""

    def test_delete_stimulus_success(self) -> None:
        """Test successful deletion of a stimulus."""
        mock_http = MockHttpClient()
        
        result = delete_stimulus(mock_http, "stimulus-001")
        
        assert result is None
        assert mock_http.delete_called
        assert mock_http.last_path == "/stimuli/stimulus-001"

    def test_delete_stimulus_path_format(self) -> None:
        """Test that delete uses correct path format."""
        mock_http = MockHttpClient()
        
        delete_stimulus(mock_http, "test-identifier-123")
        
        assert mock_http.last_path == "/stimuli/test-identifier-123"

    def test_delete_stimulus_with_special_chars(self) -> None:
        """Test deletion with special characters in identifier."""
        mock_http = MockHttpClient()
        
        delete_stimulus(mock_http, "stimulus-special_chars.v2")
        
        assert mock_http.last_path == "/stimuli/stimulus-special_chars.v2"

    def test_delete_stimulus_returns_none(self) -> None:
        """Test that delete returns None on success."""
        mock_http = MockHttpClient()
        
        result = delete_stimulus(mock_http, "any-stimulus")
        
        assert result is None

