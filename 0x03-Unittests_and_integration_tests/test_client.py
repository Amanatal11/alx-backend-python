from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    # (Keep your previous test_org here)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected URL"""

        test_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:

            mock_org.return_value = test_payload

            client = GithubOrgClient("test_org")

            result = client._public_repos_url

            self.assertEqual(
                result,
                "https://api.github.com/orgs/test_org/repos"
            )
