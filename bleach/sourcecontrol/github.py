import requests

from bleach import config
from bleach.models import pullrequest


def listPullRequests(owner, repository):
    url = _getUrl(owner, repository)
    headers = _getHeaders()
    processedResults = []

    keepFetchingResults = True
    while keepFetchingResults:
        response = requests.get(url, headers=headers)

        if response.status_code == 404:
            print("couldn't find the organization or repository")
            return []

        if response.status_code == 401:
            print("unauthorized, check your access token")
            raise Exception("unauthorized, check your access token")

        pullrequests = response.json()
        processedResults.extend(
            pullrequest.PullRequest(createdAt=pullrequestInfo['created_at'],
                                    user=pullrequestInfo['user']['login'],
                                    title=pullrequestInfo['title'])
            for pullrequestInfo in pullrequests
        )

        if response.links and 'next' in response.links:
            url = response.links['next']['url']
        else:
            keepFetchingResults = False

    return processedResults


def _getUrl(owner, repository):
    URL_TEMPLATE = "https://api.github.com/repos/{owner}/{repository}/pulls{params}"
    params = "?state=open&sort=created_at&direction=asc"
    url = URL_TEMPLATE.format(owner=owner, repository=repository, params=params)
    return url


def _getHeaders():
    headers = {}
    if config.CONFIG["githubAccessToken"]:
        headers['Authorization'] = 'token ' + config.CONFIG["githubAccessToken"]
    return headers
