from functions import *
import telegram
import schedule
import time

my_token = "1702806418:AAFNyJ2J_seTRLid2nsUc40xeLf3l2c1JvI"
# my_chat_id = "1769603089" #alfred 봇 개인챗
my_chat_id = "@aaaalfred" #aaaalfred 채널

week = datetime.today().weekday()
bot = telegram.Bot(token = my_token)
updates = bot.getUpdates()

def sendIndustries():
    result_list = hankyungIndustry()['산업리포트'][today()]
    content = '[{}의 산업리포트] \n\n'.format(today())
    
    for i in result_list:
        title = i['제목']
        url = i['링크']
        item = title + '\n' + url  + '\n\n'
        content = content + item
    
    print('텔레그렘 메시지 발송:')
    print(content)
    print('끝')
    bot.sendMessage(chat_id = my_chat_id, text=content)

sendIndustries()

# def job():
#     if week < 5:
#         sendIndustries()
#     else:
#         pass

# 매일 10:30 에 실행
# schedule.every().day.at("07:00").do(job)
# schedule.every(10).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)