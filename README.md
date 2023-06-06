# Discord Chat Bot

This is a simple Discord chat bot that listens to incoming messages from all users. The bot will generate a response based on the user's message and send it either privately or in the channel where the message was sent from. The bot uses a module named responses to generate replies for incoming messages.

## Installation

To run the Discord bot, you need to install the `discord` library. You can install it using `pip`:

## Setup Instructions

Clone the repository: git clone https://github.com/username/repo.git

Note: This bot requires Python 3.7+ to run.

## Usage

To start the bot, simply run:

python bot.py

This script will initiate the bot and connect it to your Discord server using the token you provide.

## Configuration

The bot requires a Discord token to function. Make sure to replace the following line in bot.py with your Discord Bot's token:
TOKEN = 'your_discord_token_here'

## Interacting with the Bot

Any message sent to a channel where the bot is active will be received by the bot.
If the message starts with ?, the bot will respond to the user privately.
If not, the bot will respond directly in the channel.

## Contribution

Feel free to contribute to this project by creating a pull request. Please ensure that your code passes all existing tests and lint checks.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions, feel free to open an issue.
