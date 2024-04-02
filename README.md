# `unnamed-color-bot`
> A convenient and unnessecary color tool, right within discord.

![License][license-shield]
![Stars][stars-shield]
# ![Banner](banner.png)

i don't know why i made this, please send help

## Usage <!-- Using the product -->
You can [**invite the bot here**](https://discord.com/api/oauth2/authorize?client_id=837141419650449418&scope=applications.commands).
Please remember to report any bugs, suggestions, or issues.

This bot utilizes discord slash commands, you can view them all on Discord.

## Contributing <!-- Using the source -->
This repository split into 2 main parts.
- `commands/`
- `cloud_function/`

### `commands/`
This is the local python project with the script that you will most likely be running.

1. Create a `.env` file.
  ```
  APPLICATION_ID=
  BOT_TOKEN=
  ```
2. Run `pipenv install` to install all of the dependencies for the script.
3. Run `pipenv run main` to run the script.

### `cloud_function/`
The bot is hosted using Google Cloud Functions, this folder contains the files that are uploaded.

1. Inside `main.py`, replace the string in `PUBLIC_KEY = ""` with the public key of your application.

---

*empathy included • [**@cysabi**](https://github.com/cysabi) • [cysabi.github.io](https://cysabi.github.io)*

<!-- markdown links & imgs -->
[stars-shield]: https://img.shields.io/github/stars/LeptoFlare/unnamed-color-bot.svg?style=social
[license-shield]: https://img.shields.io/github/license/LeptoFlare/unnamed-color-bot.svg?style=flat
