from 政府資料處理 import *

"""
題目 1:
請透過上方 api 文件，找出 "歸化國籍人數按原屬國籍及性別分" 的資料，並把你/妳如何操作的步驟寫出
題目 2:
請透過上方 api 文件，找出 "110年 嬰兒出生數按性別及生母單一年齡分（按登記）" 的資料 (所有頁數)
題目 3:
接續上題，將媽媽未滿18歲的資料歸納出來
"""

dataGetter = DataGetter()
dataGetter.request_url("https://www.ris.gov.tw/rs-opendata/api/Main/docs/v1")
CaseOne("歸化國籍人數按原屬國籍及性別分")
CaseTwo("嬰兒出生數按性別及生母單一年齡分（按登記）", 110)
CaseThree(18)