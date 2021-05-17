import re

from discord_interactions import InteractionResponseType


def main(json):
    options = {option["name"]: option["value"] for option in json["data"]["options"]}
    try:
        color = Color(options["color"])
    except Exception:
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "flags": 64,
            "data": {"content": "🚫 Invalid color format"},
        }
    return {
        "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "embeds": [
                {
                    "author": {
                        "name": f"#{str(color)}",
                        "url": f"https://coolors.co/{str(color)}",
                    },
                    "color": color.color,
                    "image": {
                        "url": f"https://singlecolorimage.com/get/{str(color)}/256x256"
                    },
                }
            ]
        },
    }


class Color:
    def __init__(self, color):
        self.color = self.parse_color(color)

    def __str__(self):
        return hex(self.color)[2:].zfill(6)

    @staticmethod
    def parse_color(color: str) -> int:
        """Attempt to convert a color in any arbitrary format into a hex string."""
        color = color.lower()
        if color.startswith("#"):
            color = color[1:]
        if color.startswith("rgb"):
            color = re.sub(r"[^1-9,]", "", color)
            color = color.split(",")
            color = "".join(hex(int(c))[2:].zfill(2) for c in color)
        return int(color, 16)
