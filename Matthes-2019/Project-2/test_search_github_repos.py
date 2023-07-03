import unittest
from search_github_repos import get_github_status, query_github_repos


class GitHubQueryTestCase(unittest.TestCase):
    """Test an API call to GitHub
    """
    def test_get_github_status(self):
        istatus = get_github_status('python')
        self.assertEqual(istatus, 200)

    def test_n_items(self):
        idict = query_github_repos('python')
        n_items = len(idict['items'])
        n_repos = idict['total_count']
        self.assertGreater(n_items, 29)
        self.assertGreater(n_repos, 1_000_000)



if __name__ == '__main__':
    unittest.main()
