import telebot

API_KEY = # Here you put your token

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["pizza"])
def pizza(message):
    bot.send_message(message.chat.id, "Pizza is on its way to your house: Estimated wait time 20 minutes")

@bot.message_handler(commands=["hamburger"])
def hamburger(message):
    bot.send_message(message.chat.id, "Hamburger is on its way to your house: Estimated wait time 15 minutes")

@bot.message_handler(commands=["salad"])
def salad(message):
    bot.send_message(message.chat.id, "Sorry, we don't have salad. To start over, use the /start command")

@bot.message_handler(commands=["option1"])
def option1(message):
    text = """
    What do you want? (Click on an option)
    /pizza Pizza
    /hamburger Hamburger
    /salad Salad"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["option2"])
def option2(message):
    bot.send_message(message.chat.id, "To submit a complaint, send an email to complaints@blabla.com")

@bot.message_handler(commands=["option3"])
def option3(message):
    bot.send_message(message.chat.id, "Thank you! Max sends a hug back!")

def verify_message(message):
    return True

@bot.message_handler(func=verify_message)
def respond(message):
    # Add your code to handle the message here
    pass

bot.polling()
