from utils import decorator
import functions

def init(update, context):
    txt = functions.general.txtReader('source')
    context.bot.send_message(update.message.chat_id, text=txt, parse_mode='HTML')