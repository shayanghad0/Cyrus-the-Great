from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define the buttons
keyboard = [
    ['deposit', 'withdrawal'],
    ['support', 'my account']
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('[              bet.                 ]', reply_markup=reply_markup)

# Message handler for button presses
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == 'deposit':
        update.message.reply_text('You pressed Deposit')
    elif text == 'withdrawal':
        update.message.reply_text('You pressed Withdrawal')
    elif text == 'support':
        update.message.reply_text('You pressed Support')
    elif text == 'my account':
        update.message.reply_text('You pressed My Account')
    else:
        update.message.reply_text('Unknown command')

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("8156484797:AAHcNCW4oX29IwYW8ud-kqRuYQsL58XBDC8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()