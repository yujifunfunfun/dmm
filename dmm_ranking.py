import requests
from bs4 import BeautifulSoup
import re
from logger import set_logger
logger = set_logger(__name__)



def fetch_dmm_ranking_data():
    ranking_url = 'https://www.dmm.com/mono/hobby/-/ranking/=/mode=figure/term=week/rank=1_20/'
    res = requests.get(ranking_url)
    soup = BeautifulSoup(res.text, "html.parser")
    names = soup.select("div.data > p")
    prices = soup.select("div.data > div.red")
    urls = soup.select("td.bd-b > a")
    print(len(prices))
    print(len(urls))
    
    name_price_url_jan_list = []
    for name_elem,price_elem,url_elem in zip(names,prices,urls):
        try:
            name = name_elem.text
        
            price = price_elem.text
            p = r'(.*)円'  
            price = re.search(p, price).group(1)      
            price = re.sub(r'\D', '', price) 

            url = url_elem.get('href')
            url = 'https://www.dmm.com' + url
            
            res = requests.get(url)
            item_detail_soup = BeautifulSoup(res.text, "html.parser")
            jan_elem = item_detail_soup.select("table.mg-b20")

            jan_elem_text = jan_elem[0].text
            p = r'[0-9]{13}'  
            jan = re.search(p, jan_elem_text).group(0)
        except Exception as e:
            logger.info(e)
            name = 'None'
            price = 999999
            url = 'None'
            jan = 'None'
        
        name_price_url_jan_list.append([name,price,url,jan])
    print(name_price_url_jan_list)
    


if __name__ == "__main__":
    fetch_dmm_ranking_data()