import requests

url_prefix = 'https://api.github.com/search/repositories?q=language:'
url_suffix = '&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

def get_github_status(language):
    """Returns the status code of a API call to github for
    for repositories on a particular language
    """
    language = language.lower()
    url = url_prefix+language+url_suffix
    r = requests.get(url, headers=headers)
    return r.status_code

def query_github_repos(language):
    """search GitHub for repositories on a particular language
    if the query is successful (Status 200) returns a dictionary
    """
    repo_status = get_github_status(language)
    if repo_status == 200:
        language = language.lower()
        url = url_prefix+language+url_suffix
        r = requests.get(url, headers=headers)
        # Store API response in a variable.
        response_dict = r.json()
        return response_dict
