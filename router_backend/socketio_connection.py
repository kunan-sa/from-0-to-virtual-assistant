import uuid
from socketio import AsyncServer
from sanic.log import logger

from slack_integration import SlackIntegration, session_to_channel

session_to_sid = {}

ERROR_CONNECT_TO_SLACK = "Could not connect to operator"
ERROR_SEND_MESSAGE = "Could not send message"


sio = AsyncServer(async_mode="sanic", cors_allowed_origins=[])  # '*'
conn = SlackIntegration()

@sio.on("connect")
async def connect(sid, environ):
    logger.info(f"User {sid} connected to socketIO endpoint.")


@sio.on("disconnect")
async def disconnect(sid):
    logger.info(f"User {sid} disconnected from socketIO endpoint.")


@sio.on("session_request")
async def session_request(sid, data):
    if data is None:
        data = {}
    if "session_id" not in data or data["session_id"] is None:
        data["session_id"] = uuid.uuid4().hex
    # session persistence by default
    sio.enter_room(sid=sid, room=data["session_id"])
    session_to_sid[data["session_id"]] = sid
    await sio.emit(event="session_confirm", data=data["session_id"], room=sid)


@sio.on("user_uttered")
async def received_user_message(sid, data):
    if not data.get("message"):
        return  # eco

    session_id = data["session_id"]
    
    channel_id = session_to_channel.get(session_id)
    if channel_id is None:
        channel_id = await conn.connect_to_slack(session_id)
        if channel_id is None:
            return await sio.emit("bot_uttered", {"text": ERROR_CONNECT_TO_SLACK}, room=session_id)
    
    if data["message"]!="/get_started":
        error = await conn.send_to_operator(channel_id, data["message"])

    if error == "channel_not_found":
        channel_id = await conn.connect_to_slack(session_id)
        if channel_id is None:
            return await sio.emit("bot_uttered", {"text": ERROR_CONNECT_TO_SLACK}, room=session_id)
        await conn.send_to_operator(channel_id, data["message"])

    elif error is not None:
        await sio.emit("bot_uttered", {"text": ERROR_SEND_MESSAGE}, room=session_id)
