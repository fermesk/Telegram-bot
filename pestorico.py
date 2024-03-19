from telegram.ext import Update, CommandHandler, MessageHandler, Filters, CallbackContext,ContextTypes
from telegram import update


TOCKEN = "7079853699:AAGEOCN9PFOaHII8Sy5s4M3v8TT3JHL7Qb0"


async def start_commend(update: Update,context: ContextTypes.DEFUALT_TYPES):
    await update.message.reply_text('Hello, thanks for chatting with me, I"m pesto rico')

async def help_commend(pdate: Update,context: ContextTypes.DEFUALT_TYPES):
    await update.message.reply_text('Hello, I"m pesto rico, please type something so i can respond')


#responces
def handler_response(rext: str )→ str:
    pass


