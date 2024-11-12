from src.utils.constants import Paths
import requests
import subprocess

class BitBucket:

    def __init__(self, username, password, server_url):
        self.username = username
        self.password = password
        self.server_url = server_url
        self.url_templates = {
            'project_key': '{bitbucket_server}/rest/api/1.0/projects/{project_key}/repos?start={start}&limit={limit}',
            'base': '{bitbucket_server}/rest/api/1.0/repos?start={start}&limit={limit}'
        }


    def get_repositories(self, project_key = None, start=0, limit=100):
        """Fetch all repositories from the specified project or across all projects."""
        repos = []

        while True:
            url = self.url_builder(start, limit, project_key)
            print('url: ', url)
            response = requests.get(url, auth=(self.username, self.password))
            response.raise_for_status()  # Raises an error for a bad response

            data = response.json()
            repos.extend(data["values"])

            if data["isLastPage"]:
                break
            start += limit

        return repos

    def clone_repositories(repos):
        """Clone each repository to the local machine."""
        for repo in repos:
            clone_url = repo["links"]["clone"][0]["href"]
            repo_name = repo["slug"]
            print(f"Cloning {repo_name}...")
            subprocess.run(["git", "clone", clone_url])

    def url_builder(self, start, limit, project_key=None):
        if project_key:
            url = self.url_templates['project_key'].format(bitbucket_server=self.server_url, project_key=project_key,
                                                           start=start, limit=limit)
        else:
            url = self.url_templates['base'].format(bitbucket_server=self.server_url, start=start, limit=limit)
        return url



if __name__ == '__main__':
    print('Testing')
