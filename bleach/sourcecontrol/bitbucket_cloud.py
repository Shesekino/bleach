import base64
import requests

from bleach import config
from bleach.models import pullrequest


def listPullRequests(owner, repository):
    url = _getUrl(owner, repository)
    response = requests.get(url, headers=_getHeaders())

    if response.status_code == 404:
        print("couldn't find the organization or repository")
        return []

    if response.status_code == 401:
        print("unauthorized, check your username or password")
        raise Exception("unauthorized, check your username or password")

    processedResponse = response.json()

    # TODO handle response pages

    pullrequests = processedResponse['values']
    # created_on , title , author.username

    filteredInfo = [
        pullrequest.PullRequest(createdAt=pullrequestInfo['created_on'],
                                user=pullrequestInfo['author']['username'],
                                title=pullrequestInfo['title'])
        for pullrequestInfo in pullrequests
    ]

    return filteredInfo


def _getUrl(owner, repository):
    URL_TEMPLATE = "https://api.bitbucket.org/2.0/repositories/{owner}/{repository}/pullrequests{params}"
    params = "?state=OPEN"
    url = URL_TEMPLATE.format(owner=owner, repository=repository, params=params)
    return url


def _getHeaders():
    headers = {}
    authorizationString = "{username}:{password}".format(
        username=config.CONFIG["bitbucketCloudUser"], password=config.CONFIG["bitbucketCloudPassword"])
    encodedAuthorizationString = base64.b64encode(bytes(authorizationString, 'utf-8'))
    headers["Authorization"] = "basic %s" % encodedAuthorizationString.decode('utf-8')
    return headers
