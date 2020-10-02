from sanic import Sanic
from sanic import response
from sanic.request import Request
from sanic.log import logger
from sanic_cors import CORS

from socketio_connection import sio, session_to_sid
from slack_integration import SlackIntegration, channel_to_session, session_to_channel


FINAL_MESSAGE = 'End'


app = Sanic("router")

app.config.RESPONSE_TIMEOUT = 60 * 60
app.config.REQUEST_TIMEOUT = 60 * 5
app.config.CORS_AUTOMATIC_OPTIONS = True
app.config.CORS_SUPPORTS_CREDENTIALS = True
CORS(app, resources={r"/*": {"origins": "*"}})

sio.attach(app, socketio_path="/socket.io")


@app.route("/", methods=["GET"])
async def health(request):
    return response.json({"status": "ok"})


@app.route("/webhook", methods=["GET", "POST"])
async def webhook(request):
    """ Webhook to receive messages from slack. """
    output = request.json
    event = output.get("event", {})
    operator_message = event.get("text", "")

    if "challenge" in output:
        return response.json(output.get("challenge"))

    elif SlackIntegration.is_operator_message(output):
        channel_id = SlackIntegration.channel_from_message(output)
        session_id = channel_to_session.get(channel_id)
        if session_id is None:
            return response.text("")

        await sio.emit("bot_uttered", {"text": operator_message}, room=session_id)

        if operator_message == FINAL_MESSAGE:
            channel_to_session.pop(channel_id, None)
            session_to_channel.pop(session_id, None)
            sio.leave_room(sid=session_to_sid[session_id], room=session_id)
            session_to_sid.pop(session_id, None)

    return response.text("")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True, access_log=True, ssl=None)
