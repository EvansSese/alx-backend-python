#!/usr/bin/env python3
"""Test client suite"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGitHub client suite"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Create an instance of GithubOrgClient"""
        github_org_client = GithubOrgClient(org_name)
        result = github_org_client.org()
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == '__main__':
    unittest.main()
