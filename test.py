import requests
from bs4 import BeautifulSoup
import re



# ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
#         "AppleWebKit/537.36 (KHTML, like Gecko)" \
#         "Chrome/95.0.4638.69"

# url = 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021092583292/?dmmref=gMonoHobby_Ranking_Figure_Week'
# res = requests.get(url,headers={"User-Agent": ua})
# soup = BeautifulSoup(res.text, "html.parser")


# jan = soup.select("table.mg-b20")

list = [['【予約】ハンドスケール バーゼラルド Animation Ver.', '3445', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_202111fg095/?dmmref=gMonoHobby_Ranking_Figure_Week', '4934054029877'], ['【予約】【1月再生産分】HG 1/144 ガンダムヘリオス', '2530', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062555014_22_01/?dmmref=gMonoHobby_Ranking_Figure_Week', '2021062555014'], ['HGGBB 1/144 ガンダムリヴランスヘブン', '1738', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062555016/?dmmref=gMonoHobby_Ranking_Figure_Week', '4573102620248'], 
['【予約】ガンダムデカールNo.129 HG 1/144 ナイチンゲール用', '550', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062578998/?dmmref=gMonoHobby_Ranking_Figure_Week', '4573102621627'], ['None', 999999, 'None', 'None'], ['Figure-rise Standard トライチェイサー2000', '3286', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062575555/?dmmref=gMonoHobby_Ranking_Figure_Week', '4573102620149'], ['HGGBB 1/144 ガンダムヘリオス', '2277', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062555014/?dmmref=gMonoHobby_Ranking_Figure_Week', '4573102620163'], ['【予約】【2月再生産分】HG 1/144 ザクII', '1760', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021062553796_22_02/?dmmref=gMonoHobby_Ranking_Figure_Week', '2021062553796'], ['None', 999999, 'None', 'None'], ['【予約】30MS オプションヘアスタイルパーツVol.4 全4種 ロングヘア3［...', '660', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021092590336/?dmmref=gMonoHobby_Ranking_Figure_Week', '2021092590336'], ['None', 999999, 'None', 'None'], ['【予約】30MS オプションヘアスタイルパーツVol.4 全4種 ロングヘア4［...', '660', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021092590337/?dmmref=gMonoHobby_Ranking_Figure_Week', 
'2021092590337'], ['None', 999999, 'None', 'None'], ['None', 999999, 'None', 'None'], ['None', 999999, 'None', 'None'], ['None', 999999, 'None', 'None'], ['None', 999999, 'None', 'None'], ['【予約】30MS オプションヘアス タイルパーツVol.4 全4種 ミディアムヘア...', '660', 'https://www.dmm.com/mono/hobby/-/detail/=/cid=cha_2021092590335/?dmmref=gMonoHobby_Ranking_Figure_Week', '2021092590335']]



# jan = jan[0].text

# p = r'[0-9]{13}'  
# jan = re.search(p, jan).group(0)

print(len(list))

# for price in prices:
#         price = price.text
#         p = r'(.*)円'  
#         keyword = re.search(p, price).group(1)      
#         price = re.sub(r'\D', '', keyword) 
          
#         print(price)
        

# for url in urls:
#         url = url.get('href')
#         url = 'https://www.dmm.com' + url
#         print(url)
        
