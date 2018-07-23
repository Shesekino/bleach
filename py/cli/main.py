import argparse

from sourcecontrol import github
from outputs import stdout


def main(owner, repository, accessToken):
    pullrequestInfo = github.listPullRequests(owner, repository, accessToken)
    stdout.send(pullrequestInfo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get pull request status")
    parser.add_argument("owner", help="the name of the repository's owner")
    parser.add_argument("repository", help="the name of the repository to get PR status for")
    parser.add_argument("--accessToken", help="a personal access token to use for privileged repositories")
    args = parser.parse_args()
    main(args.owner, args.repository, args.accessToken)
