import slackclient

from bleach import config


def send(data):
    slackClient = slackclient.SlackClient(config.CONFIG['slackAccessToken'])

    # TODO check response for errors?
    response = slackClient.api_call(
        "chat.postMessage",
        channel=config.CONFIG['slackChannel'],
        text=data,
    )
