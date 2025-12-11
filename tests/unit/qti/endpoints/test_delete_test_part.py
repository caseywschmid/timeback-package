"""Unit tests for delete_test_part endpoint.

Tests the delete_test_part function that deletes a test part.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.delete_test_part import delete_test_part


class MockHttpClient:
    """Mock HTTP client for testing."""

    def __init__(self):
        """Initialize the mock client."""
        self.last_path: str = ""
        self.delete_called: bool = False

    def delete(self, path: str) -> None:
        """Mock DELETE request."""
        self.last_path = path
        self.delete_called = True


class TestDeleteTestPart:
    """Tests for delete_test_part endpoint."""

    def test_delete_test_part_success(self) -> None:
        """Test successful test part deletion."""
        mock_http = MockHttpClient()
        
        delete_test_part(mock_http, "test-001", "part-001")
        
        assert mock_http.delete_called
        assert mock_http.last_path == "/assessment-tests/test-001/test-parts/part-001"

    def test_delete_test_part_path_includes_both_identifiers(self) -> None:
        """Test that the path includes both test and part identifiers."""
        mock_http = MockHttpClient()
        
        delete_test_part(mock_http, "my-test-id", "my-part-id")
        
        assert mock_http.last_path == "/assessment-tests/my-test-id/test-parts/my-part-id"

    def test_delete_test_part_returns_none(self) -> None:
        """Test that delete returns None."""
        mock_http = MockHttpClient()
        
        result = delete_test_part(mock_http, "test-001", "part-001")
        
        assert result is None

    def test_delete_test_part_calls_http_delete(self) -> None:
        """Test that delete calls the HTTP delete method."""
        mock_http = MockHttpClient()
        
        delete_test_part(mock_http, "test-001", "part-001")
        
        assert mock_http.delete_called

    def test_delete_test_part_with_special_characters(self) -> None:
        """Test deletion with special characters in identifiers."""
        mock_http = MockHttpClient()
        
        delete_test_part(mock_http, "test-123-abc", "part-456-xyz")
        
        assert mock_http.last_path == "/assessment-tests/test-123-abc/test-parts/part-456-xyz"

