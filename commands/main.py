"""A Script to create and delete slash commands."""
import os
import requests


slash_color = lambda: make_request(
    endpoint="commands",
    json={
        "name": "color",
        "description": "Identify and display a color that you choose",
        "options": [
            {
                "name": "color",
                "description": "The color you'd like to identify, in any format",
                "type": 3,
                "required": True,
            },
        ],
    },
)


def make_request(endpoint, json):
    r = requests.post(
        url=f"https://discord.com/api/v8/applications/{os.getenv('APPLICATION_ID')}/{endpoint}",
        headers={"Authorization": f"Bot {os.getenv('BOT_TOKEN')}"},
        json=json,
    )
    print(f"{json['name']}:", r.status_code)


if __name__ == "__main__":
    slash_color()
