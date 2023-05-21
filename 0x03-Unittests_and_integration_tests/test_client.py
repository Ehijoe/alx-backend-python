#!/usr/bin/env python3
"""Tests for client.py."""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Tests for the Github client."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    def test_org(self, org):
        """Test the org property."""
        with patch("client.get_json", return_value="Response") as get:
            github_client = GithubOrgClient(org)
            self.assertEqual(github_client.org, "Response")
            self.assertEqual(github_client.org, "Response")
            get.assert_called_once_with(github_client.ORG_URL.format(org=org))
