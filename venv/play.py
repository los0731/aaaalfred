from crawl import *
from stocks import *
import csv
import time
date = time.strftime('%Y%m', time.localtime(time.time()))

for idx, i in enumerate(stocks_list()):
    print('##### 크롤시작:\n____________________')
    data, rowData = crawl(i)
    print('\n\n\n##### data:\n____________________')
    pp(data, width=30)
    print('\n\n\n##### rowData:\n____________________')
    pp(rowData, width=30)
    
    

    with open("results/data{}.csv".format(date), "a", encoding='utf-8-sig', newline='') as f:
        wr = csv.writer(f)
        if idx == 0:
            wr.writerow(list(rowData.keys()))
        wr.writerow(list(rowData.values()))
    f.close()

    if (idx+1)%400 == 0:
        pp('20분간 쉽니다. :-)')
        time.sleep(1200)
    else:
        time.sleep(8)
    print('\n\n\n\n\n')