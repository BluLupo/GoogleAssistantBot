import config
from functions.general import message
def init(update, context):
    hashtag = ['#vendo', '#compro', '#scambio']
    if update.message.text is not None:
        print(update.message.text)
        if update.message.chat_id == config.mercatino: #and not(update.message.from_user.id in config.LIST_OF_ADMINS):
            if str(update.message.text).startswith(tuple(hashtag)):
                txt = "<b>ATTENZIONE</b>\nIl tuo messaggio non rispetta le linee guida del gruppo, controlla il messaggio fissato per saperne di più!"
                context.bot.delete_message(update.message.chat_id, update.message.message_id)
                message(update, context, txt)

        