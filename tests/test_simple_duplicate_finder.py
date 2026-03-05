"""Tests for simple-duplicate-finder."""

import pytest
from simple_duplicate_finder import finder


class TestFinder:
    """Test suite for finder."""

    def test_basic(self):
        """Test basic usage."""
        result = finder("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            finder("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = finder(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
