"""Unit tests for delete_section endpoint.

Tests the delete_section function that deletes a section.
"""

from typing import Any, Dict
import pytest

from timeback.services.qti.endpoints.delete_section import delete_section


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


class TestDeleteSection:
    """Tests for delete_section endpoint."""

    def test_delete_section_success(self) -> None:
        """Test successful section deletion."""
        mock_http = MockHttpClient()
        
        delete_section(mock_http, "test-001", "part-001", "section-001")
        
        assert mock_http.delete_called
        expected_path = "/assessment-tests/test-001/test-parts/part-001/sections/section-001"
        assert mock_http.last_path == expected_path

    def test_delete_section_path_includes_all_identifiers(self) -> None:
        """Test that the path includes all identifiers."""
        mock_http = MockHttpClient()
        
        delete_section(mock_http, "my-test", "my-part", "my-section")
        
        expected_path = "/assessment-tests/my-test/test-parts/my-part/sections/my-section"
        assert mock_http.last_path == expected_path

    def test_delete_section_returns_none(self) -> None:
        """Test that delete returns None."""
        mock_http = MockHttpClient()
        
        result = delete_section(mock_http, "test-001", "part-001", "section-001")
        
        assert result is None

    def test_delete_section_calls_http_delete(self) -> None:
        """Test that delete calls the HTTP delete method."""
        mock_http = MockHttpClient()
        
        delete_section(mock_http, "test-001", "part-001", "section-001")
        
        assert mock_http.delete_called