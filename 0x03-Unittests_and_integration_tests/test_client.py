#!/usr/bin/env python3
"""Test client suite"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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
        mock_get_json.return_value = MagicMock()
        result = github_org_client.org()
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertIsInstance(result, MagicMock)

    def test_public_repos_url(self):
        """Create a known payload for mocking the org method"""
        known_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value=known_payload):
            github_org_client = GithubOrgClient("testorg")
            result = github_org_client._public_repos_url
            self.assertEqual(result, known_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock,
           return_value="https://api.github.com/orgs/testorg/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Create a known payload for mocking the get_json method"""
        known_payload = [{"name": "repo1"}, {"name": "repo2"},
                         {"name": "repo3"}]
        mock_get_json.return_value = known_payload
        github_org_client = GithubOrgClient("testorg")
        result = github_org_client.public_repos()
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/testorg/repos")
        expected_result = ["repo1", "repo2", "repo3"]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
