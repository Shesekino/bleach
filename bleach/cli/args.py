import argparse


def getCommandlineArgs():
    parser = argparse.ArgumentParser(description="Get pull request status")

    parser.add_argument("owner", help="the name of the repository's owner")
    parser.add_argument("repository", help="the name of the repository to get PR status for")
    parser.add_argument("--accessToken", help="a personal access token to use for privileged repositories")
    parser.add_argument("--outputMethod", help="output method. may be stdout (default) or slack (requires OAuth token)",
                        default="stdout")

    return parser.parse_args()
