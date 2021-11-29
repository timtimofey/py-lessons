import telebot
TOKEN = '2089209807:AAGHWZ4k0UR0qkOVr6wRqk81J7N8yIgjGvo'
def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text

            tb.send_message(chatid, text)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()