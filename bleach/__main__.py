from bleach import config
from bleach.cli import args
from bleach.outputs import slack
from bleach.outputs import stdout
from bleach.sourcecontrol import github
from bleach.formatters import oldest_requests
from bleach.sourcecontrol import bitbucket_cloud


def main(owner, repository):
    sourceControl = config.CONFIG["sourceControl"]
    if sourceControl == 'github':
        pullrequestInfo = github.listPullRequests(owner, repository)
    elif sourceControl == 'bitbucket':
        pullrequestInfo = bitbucket_cloud.listPullRequests(owner, repository)
    else:
        raise Exception("invalid source control %s" % sourceControl)

    formattedOutput = oldest_requests.doFormat(pullrequestInfo)

    outputMethod = config.CONFIG["outputMethod"]
    if outputMethod == 'stdout':
        stdout.send(formattedOutput)
    elif outputMethod == 'slack':
        slack.send(formattedOutput)
    else:
        raise Exception("invalid output method %s" % outputMethod)

def pr(owner, repository):
    main(owner, repository)  # :genius:

def branch(owner, repository, primary, secondary):
    # who needs to check the optional parameters?
    missingCommits = github.missingCommits(owner, repository, primary, secondary)
    # TODO format the output
    TEMPLATE_MISS = "*{repo}*\nprimary branch {primary} seems to be missing commits from secondary branch {secondary}"
    TEMPLATE_OK = "*{repo}*\nprimary branch {primary} seems to be synced with secondary branch {secondary}"
    if missingCommits:
        badlyFormattedOutput = TEMPLATE_MISS.format(repo=repository, primary=primary, secondary=secondary)
    else:
        badlyFormattedOutput = TEMPLATE_OK.format(repo=repository, primary=primary, secondary=secondary)
    outputMethod = config.CONFIG["outputMethod"]
    if outputMethod == 'stdout':
        stdout.send(badlyFormattedOutput)
    elif outputMethod == 'slack':
        slack.send(badlyFormattedOutput)
    else:
        raise Exception("invalid output method %s" % outputMethod)

if __name__ == "__main__":
    args = args.getCommandlineArgs()

    # parsers can and should use subcommand set_default to invoke the proper command
    # https://docs.python.org/3/library/argparse.html
    # instead of this silly stuff repeating itself
    if args.subparser_name == 'pr':
        pr(args.owner, args.repository)

    if args.subparser_name == 'branch':
        branch(args.owner, args.repository, args.primary, args.secondary)

    # durrr
    # main(args.owner, args.repository)
