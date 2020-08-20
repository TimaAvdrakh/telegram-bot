TOKEN = "1358610764:AAGGGIV8eIi8P8Nl3hl5FfEThhqEhd-x0ZY"

import logging
from telegram.ext import (Updater,
                          CommandHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! Use /set <seconds> to set a timer')

def alarm(context):
    job = context.job
    context.bot.send_message(job.message, text='Beeeep! Beeep')

def set_timer(update,context):
    pass

def unset_timer(update,context):
    pass

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

    dp.add_handler(CommandHandler("upset",unset_timer,pass_chat_data=True))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()