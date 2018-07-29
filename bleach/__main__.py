import os

from bleach.cli import args
from bleach.outputs import slack
from bleach.outputs import stdout
from bleach.formatters import default
from bleach.sourcecontrol import github


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
