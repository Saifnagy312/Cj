import telebot, g4f

bot = telebot.telebot('8590136314:AAFuf8anUjqiy-YhxdFREE5q1ceGX2Iz9rm')

@bot.massage_handler(func=lambda m: True)
def chat(m):
    reply = g4f.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": m.text}])
    bot.reply_to(m, reply)

    bot.polling()