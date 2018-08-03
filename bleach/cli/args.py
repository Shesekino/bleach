import sys
import argparse

from bleach import config


def getCommandlineArgs():
    parser = argparse.ArgumentParser(description="Get pull request status")

    parser.add_argument("owner", help="the name of the repository's owner")
    parser.add_argument("repository", help="the name of the repository to get PR status for")
    parser.add_argument("--outputMethod", help="output method. may be stdout (default) or slack (requires OAuth token)",
                        default="stdout")
    parser.add_argument("--daysOpenThreshold", help="show only pull requests open longer than this number (days)",
                        type=int, default=2)
    parser.add_argument("--countToDisplay", help="how many pull requests to display", type=int, default=5)

    args = parser.parse_args()
    _validateArgs(args)
    _loadArgsToConfig(args)
    return args


def _validateArgs(args):
    if args.daysOpenThreshold < 0:
        print("--daysOpenThreshold must be non-negative")
        sys.exit(1)

    if args.countToDisplay < 0:
        print("--countToDisplay must be non-negative")
        sys.exit(1)

    if args.outputMethod not in ['slack', 'stdout']:
        print("--outputMethod must be stdout or slack")
        sys.exit(1)

    if args.outputMethod == 'slack':
        if not config.CONFIG['slackChannel']:
            print("must set a slack channel for slack integration")
            sys.exit(1)
        if not config.CONFIG['slackAccessToken']:
            print("must set a slack access token for slack integration")
            sys.exit(1)


def _loadArgsToConfig(args):
    config.CONFIG["outputMethod"] = args.outputMethod
    config.CONFIG["daysOpenThreshold"] = args.daysOpenThreshold
    config.CONFIG["countToDisplay"] = args.countToDisplay
