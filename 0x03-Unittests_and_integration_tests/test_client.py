#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing asdasdsa"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(data)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """an integration test for githuborg client"""

    @classmethod
    def setUpClass(cls):
        """ set up class befor each method"""
        config = {'return_value.json.side_effect':
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """add some more integration"""
        tst_cls = GithubOrgClient('Facebook')
        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down after each class"""
        cls.get_patcher.stop()
