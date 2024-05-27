import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "test_org"})
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test TestGithubOrgClient.test_public_repos
        return the correct value
        """
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=Mock) as mock_public:
            mock_public.return_value = "https://api.github.com/repos/test"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [p["name"] for p in payloads]
            self.assertEqual(result, expected)

            mock_json.assert_called_once()
            mock_public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test TestGithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
        (org_payload(), repos_payload(), expected_repos(), apache2_repos())
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get for all test cases"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Side effect to return different payloads based on the URL
        def side_effect(url):
            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                return Mock(json=lambda: cls.org_payload)
            elif url == cls.org_payload['repos_url']:
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: [])

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        client = GithubOrgClient(self.org_payload['login'])
        result = client.public_repos()

        # Assert that the result matches the expected repos
        self.assertEqual(result, self.expected_repos)

        # Assert that requests.get was called with the correct URL
        self.mock_get.assert_called_with(self.org_payload['repos_url'])


if __name__ == "__main__":
    unittest.main()
