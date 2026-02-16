#!/usr/bin/env python3
"""Unit tests for utils.get_json"""

import unittest
from unittest.mock import patch, Mock
import utils


class TestGetJson(unittest.TestCase):
    """Test cases for utils.get_json"""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test that get_json returns expected payload"""

        test_url = "http://example.com"
        test_payload = {"key": "value"}

        # Create mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call function
        result = utils.get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
