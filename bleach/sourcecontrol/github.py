import requests


def listPullRequests(owner, repository, accessToken=None):
    headers = {}
    if accessToken:
        headers['Authorization'] = 'token ' + accessToken

    params = "?state=open&sort=created_at&direction=asc"
    url = "https://api.github.com/repos/{owner}/{repository}/pulls{params}".format(
        owner=owner, repository=repository, params=params)
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print("couldn't find the owner/repository/whatever")
        return []

    if response.status_code == 401:
        print("unauthorized")
        raise Exception("unauthorized, check your accessToken")

    processedResponse = response.json()
    filteredInfo = [
        {
            "createdAt": pullrequestInfo['created_at'],
            "user": pullrequestInfo['user']['login'],
        }
        for pullrequestInfo in processedResponse
    ]

    return filteredInfo
