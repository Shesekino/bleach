import requests


def listPullRequests(owner, repository, accessToken):
    params = "?state=open&sort=created_at&direction=asc"
    url = "https://api.github.com/repos/{owner}/{repository}/pulls{params}".format(
        owner=owner, repository=repository, params=params)
    response = requests.get(url)
    processedResponse = response.json()

    filteredInfo = [
        {
            "createdAt": pullrequestInfo['created_at'],
            "user": pullrequestInfo['user']['login'],
        }
        for pullrequestInfo in processedResponse
    ]

    return filteredInfo
