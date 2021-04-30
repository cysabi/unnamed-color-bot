from flask import jsonify
from discord_interactions import verify_key, InteractionType, InteractionResponseType

import color


PUBLIC_KEY = ""


def handler(request):
    # Verify request
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    if (
        signature is None
        or timestamp is None
        or not verify_key(request.data, signature, timestamp, PUBLIC_KEY)
    ):
        return "Bad request signature", 401

    # Automatically respond to pings
    if request.json and request.json.get("type") == InteractionType.PING:
        return jsonify({"type": InteractionResponseType.PONG})

    # Pass through
    if request.json["type"] == InteractionType.APPLICATION_COMMAND:
        if request.json["data"]["name"] == "color":
            return jsonify(color.main(request.json))
