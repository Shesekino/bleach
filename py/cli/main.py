import os

from cli import args
from outputs import slack
from outputs import stdout
from formatters import default
from sourcecontrol import github


def main(owner, repository, outputMethod, accessToken=None):
    pullrequestInfo = github.listPullRequests(owner, repository, accessToken)

    formattedOutput = default.doFormat(pullrequestInfo)

    if outputMethod == 'stdout':
        stdout.send(formattedOutput)
    elif outputMethod == 'slack':
        slack.send(formattedOutput)
    else:
        raise Exception("invalid output method %s" % outputMethod)

if __name__ == "__main__":
    args = args.getCommandlineArgs()

    accessToken = args.accessToken
    if 'BLEACH_GITHUB_ACCESS_TOKEN' in os.environ:
        accessToken = os.environ['BLEACH_GITHUB_ACCESS_TOKEN']

    main(args.owner, args.repository, args.outputMethod, accessToken)
