from bleach import config
from bleach.cli import args
from bleach.outputs import slack
from bleach.outputs import stdout
from bleach.sourcecontrol import github
from bleach.formatters import oldestRequests


def main(owner, repository):
    pullrequestInfo = github.listPullRequests(owner, repository)

    formattedOutput = oldestRequests.doFormat(pullrequestInfo)

    outputMethod = config.CONFIG["outputMethod"]
    if outputMethod == 'stdout':
        stdout.send(formattedOutput)
    elif outputMethod == 'slack':
        slack.send(formattedOutput)
    else:
        raise Exception("invalid output method %s" % outputMethod)

if __name__ == "__main__":
    args = args.getCommandlineArgs()
    main(args.owner, args.repository)
