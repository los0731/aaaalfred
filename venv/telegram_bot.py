from functions import *
import telegram

my_token = "1702806418:AAFNyJ2J_seTRLid2nsUc40xeLf3l2c1JvI"
# my_chat_id = "1769603089" #alfred 봇 개인챗
my_chat_id = "@aaaalfred" #aaaalfred 채널
# today = datetime.today().strftime("%Y-%m-%d")
yesterday = datetime.today() - timedelta(1)
yesterday = yesterday.strftime("%Y-%m-%d") 

bot = telegram.Bot(token = my_token)
updates = bot.getUpdates()

def sendIndustries():
    result_list = hankyungIndustry()['산업리포트'][yesterday]
    content = '[{}의 산업리포트] \n\n'.format(yesterday)
    
    for i in result_list:
        title = i['제목']
        url = i['링크']
        item = title + '\n' + url  + '\n\n'
        content = content + item
        
    # print(content)
    bot.sendMessage(chat_id = my_chat_id, text=content)

sendIndustries()