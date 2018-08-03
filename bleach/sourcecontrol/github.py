import requests

from bleach import config


def listPullRequests(owner, repository):
    url = _getUrl(owner, repository)
    response = requests.get(url, headers=_getHeaders())

    if response.status_code == 404:
        print("couldn't find the organization or repository, check your access token")
        return []

    if response.status_code == 401:
        print("unauthorized")
        raise Exception("unauthorized, check your access token")

    processedResponse = response.json()
    filteredInfo = [
        {
            'createdAt': pullrequestInfo['created_at'],
            'user': pullrequestInfo['user']['login'],
            'title': pullrequestInfo['title'],
        }
        for pullrequestInfo in processedResponse
    ]

    return filteredInfo


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
