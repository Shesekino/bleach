import os
import slackclient


def send(data):
    assert 'BLEACH_SLACK_CHANNEL' in os.environ
    assert 'BLEACH_SLACK_ACCESS_TOKEN' in os.environ

    slackClient = slackclient.SlackClient(os.environ['BLEACH_SLACK_ACCESS_TOKEN'])

    # TODO check response for errors?
    response = slackClient.api_call(
        "chat.postMessage",
        channel=os.environ['BLEACH_SLACK_CHANNEL'],
        text=data,
    )
