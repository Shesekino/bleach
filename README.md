# bleach
Remove mold from your repositories :)

Bleach is a project dedicated to helping software development teams keep track of their repositories and make sure no pull request is left unattended.
Bleach may query GitHub and BitBucket repositories, and write alerts on pull requests open for too long to Slack.

## Installing
For unpriviliged users:
`pip install --user bleachrepo`

Or for priviliged users / with sudo:
`pip install bleachrepo`

## Running
For public repositories:

`python -m bleach <org> <repo>`

For example:

`python -m bleach shesekino bleach`

For private repositories:

Obtain a GitHub access token with `repo` permissions, then set it as an environment variable:

`export BLEACH_GITHUB_ACCESS_TOKEN=<access token>`

and run normally.

## Writing to Slack

Set an access token to slack:

`export BLEACH_SLACK_ACCESS_TOKEN=<access token>`

and the channel you wish to write to:

`export BLEACH_SLACK_CHANNEL=<channel>`

then run:

`python -m bleach --outputMethod slack <org> <repo>`
