import argparse

from outputs import slack
from outputs import stdout
from sourcecontrol import github


def main(owner, repository, outputMethod, accessToken=None):
    pullrequestInfo = github.listPullRequests(owner, repository, accessToken)

    if outputMethod == 'stdout':
        stdout.send(pullrequestInfo)
    elif outputMethod == 'slack':
        slack.send(pullrequestInfo)
    else:
        raise Exception("invalid output method %s" % outputMethod)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get pull request status")
    parser.add_argument("owner", help="the name of the repository's owner")
    parser.add_argument("repository", help="the name of the repository to get PR status for")
    parser.add_argument("--accessToken", help="a personal access token to use for privileged repositories")
    parser.add_argument("--outputMethod", help="output method. may be stdout (default) or slack (requires OAuth token)", default="stdout")
    args = parser.parse_args()
    main(args.owner, args.repository, args.outputMethod, args.accessToken)
