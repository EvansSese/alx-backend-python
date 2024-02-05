#!/usr/bin/env python3
"""Test client suite"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Create an instance of GithubOrgClient"""
        github_org_client = GithubOrgClient("testorg")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """
    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
