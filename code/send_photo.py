import telegram

# Token của bot
my_token = "7094401597:AAEbWC3xBgG0mMS0Xv9zcauR3053z9R6Kbw"

# Tạo bot
bot = telegram.Bot(token=my_token)

# Gửi ảnh
try:
    bot.sendPhoto(chat_id="6183307421", photo=open("alert.png", "rb"), caption="Có xâm nhập, nguy hiểm!")
    print("Ảnh đã được gửi thành công!")
except Exception as ex:
    print("Không thể gửi ảnh qua Telegram:", ex)
    print(type(ex).__name__, ex.args)
