import os


CONFIG = {
    "slackChannel": os.environ.get("BLEACH_SLACK_CHANNEL", None),
    "slackAccessToken": os.environ.get("BLEACH_SLACK_ACCESS_TOKEN", None),
    "githubAccessToken": os.environ.get("BLEACH_GITHUB_ACCESS_TOKEN", None),
    "bitbucketCloudUser": os.environ.get("BLEACH_BITBUCKET_CLOUD_USER", None),
    "bitbucketCloudPassword": os.environ.get("BLEACH_BITBUCKET_CLOUD_PASSWORD", None),
    "daysOpenThreshold": 2,
    "countToDisplay": 5,
}
