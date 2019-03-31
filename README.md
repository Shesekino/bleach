# bleach
Remove mold from your repositories :)

Bleach is a project dedicated to helping software development teams keep track of their repositories and make sure no pull request is left unattended.
Bleach may query GitHub and BitBucket repositories, and write alerts on pull requests open for too long to Slack.
Bleach may also try to make an educated guess as for whether or not two branches are out of sync. For example, a `master` branch may be expected to contain all commits from a `staging` branch, and Bleach will alert if that is not the case.

## Installing
For unpriviliged users:
`pip install --user bleachrepo`

Or for priviliged users / with sudo:
`pip install bleachrepo`

## Running & Commands

`python -m bleach <org> <repo> <command> <additional_params_for_command>`

Viable commands are:
`pr` - check the status of open pull requests of given `<repo>` in `<org>`.
`branch` - compare two branches, checking if commits are present in one branch, but not another.

### Pull requests

`pr` is used to check the status of pull requests in a given repo, and helps find pull requests that are open for too long.
for example, `python -m bleach shesekino bleach pr` will write to `stdout` a summary of pull requests open for over 2 days.

### Branch sync

`branch` is used to check for commits appearing in one branch, but not another.
This feature can be useful for repositories with a `master` branch that is expected to eventually contain all recent commits from a `staging` branch.
`python -m bleach shesekino bleach branch test-branch-discrepancy-1 test-branch-discrepancy-2` will check if there are commits in branch `test-branch-discrepancy-2` that do not appear in `test-branch-discrepancy-1`.

This feature somewhat relies on guesswork and assumptions.

## Private & public repositories

Public repositories require no special treatment.
For private repositories, obtain a GitHub access token with `repo` permissions, then set it as an environment variable:

`export BLEACH_GITHUB_ACCESS_TOKEN=<access token>`

and run normally.

## Writing to Slack

Set a webhook URL to slack:

`export BLEACH_SLACK_WEBHOOK=<webhook url>`

then run:

`python -m bleach --outputMethod slack <org> <repo> <command>`
