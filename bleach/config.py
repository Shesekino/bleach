import os


CONFIG = {
    "slackChannel": os.environ.get("BLEACH_SLACK_CHANNEL", None),
    "slackAccessToken": os.environ.get("BLEACH_SLACK_ACCESS_TOKEN", None),
    "githubAccessToken": os.environ.get("BLEACH_GITHUB_ACCESS_TOKEN", None),
}
