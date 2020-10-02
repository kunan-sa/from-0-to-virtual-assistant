# https://slack.dev/python-slackclient/basic_usage.html
from slack import WebClient
from constants import SLACK_APP_TOKEN
from time import time   
from sanic.log import logger
from constants import OPERATOR_NAME
from slack.errors import SlackApiError

ERROR_INVITATION_FAILED = " A new channel was added but the invitation fail to be sent"

session_to_channel = {}
channel_to_session = {}


class SlackIntegration:
    """ Sending messages to slack """

    def __init__(self):
        self.client = WebClient(SLACK_APP_TOKEN, run_async=True)
    
    @staticmethod
    def is_operator_message(slack_event):
        return (
            slack_event.get("event")
            and (
                slack_event.get("event", {}).get("type") == "message"
                or slack_event.get("event", {}).get("type") == "app_mention"
            )
            and slack_event.get("event", {}).get("text")
            and not slack_event.get("event", {}).get("bot_id")
            and not slack_event.get("event", {}).get("subtype")
        )

    @staticmethod
    def channel_from_message(slack_event):
        return slack_event.get("event", {}).get("channel")

    async def find_operator(self):
        try:
            response = await self.client.users_list()
            if response["ok"]:
                operators = response["members"]
                operator_id = next(filter(lambda o: o["name"] == OPERATOR_NAME, operators))["id"]
                return operator_id
        except SlackApiError as e:
            logger.error(e.response["error"])

    async def create_channel(self):
        try:
            channel_name = f"user-{str(round(time()))[6:]}"
            response = await self.client.conversations_create(
                name=channel_name, is_private=False
            )
            if response["ok"]:
                channel_id = response["channel"]["id"]
                return channel_id
        except SlackApiError as e:
            logger.error(e.response["error"])

    async def invite_to_channel(self, channel_id, operator_id):
        try:
            response = await self.client.conversations_invite(
                channel=channel_id, users=operator_id
            )
            if response["ok"]:
                return 200
        except SlackApiError as e:
            logger.error(e.response["error"])

    async def send_to_operator(self, channel_id, text_message):
        try:
            response = await self.client.chat_postMessage(channel=channel_id, text=text_message)
        except SlackApiError as e:
            logger.error(e.response["error"])
            return e.response["error"]

    async def connect_to_slack(self, session_id):
        channel_id = await self.create_channel()
        operator_id = await self.find_operator()

        if channel_id and operator_id:
            invited = await self.invite_to_channel(channel_id, operator_id)
            if invited is None:
                message = ERROR_INVITATION_FAILED
                await self.send_to_operator(operator_id, message)

            session_to_channel[session_id] = channel_id
            channel_to_session[channel_id] = session_id
            return channel_id
