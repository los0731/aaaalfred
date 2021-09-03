from crawl import *
from stocks import *
import csv
import time
date = time.strftime('%Y%m', time.localtime(time.time()))

for idx, i in enumerate(stocks_list()):
    print('##### 크롤시작:\n____________________')
    data, processedData = crawl(i)
    print('\n\n\n##### data:\n____________________')
    pp(data, width=30)
    print('\n\n\n##### processedData:\n____________________')
    pp(processedData, width=30)
    
    with open("results/data{}.csv".format(date), "a", encoding='utf-8-sig', newline='') as f:
        wr = csv.writer(f)
        if idx == 0:
            wr.writerow(list(processedData.keys()))
        wr.writerow(list(processedData.values()))
    f.close()
    
    if (idx+1)%320 == 0:
        pp('20분간 쉽니다. :-)')
        time.sleep(1200)
    else:
        time.sleep(8)

    print('\n\n\n\n\n')

print("👏👏👏 크롤완료")