TOKEN = "1358610764:AAGGGIV8eIi8P8Nl3hl5FfEThhqEhd-x0ZY"
#   Todo create telegram bot


import logging

from telegram.ext import ( Updater,
                           CommandHandler,
                           MessageHandler,
                           Filters )

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help_command(update, context):
    update.message.reply_text("HELP!! I need SOmEbOdY ")

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():
    """Starting fucking bot"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()