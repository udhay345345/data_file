import time
import requests
from bs4 import BeautifulSoup
import sys
import json
#function to webscrape data
def webscrape(link):
    try:
        page = requests.get(link)
    except Exception as e:
        error_type,error_obj,error_info = sys.exc_info()
        print("error")
    
    soup = BeautifulSoup(page.content,'html.parser')
    body  = soup.find('script',attrs={'id':'__NEXT_DATA__'})
    pydict = json.loads(body.text)
    restaurant = pydict['props']['pageProps']['initialMenuState']['restaurant']
    result = {}
    result["restaurant_name"]=restaurant["name"]
    result["restaurant_logo"] = restaurant['logo']
    result["latitude"] = float(restaurant['latitude'])
    result["longitude"] = float(restaurant['longitude'])
    result["cuisine_tags"] = restaurant['cuisineString'].split(", ")
    menu_items = pydict['props']['pageProps']['initialMenuState']['menuData']['items']
    items = []
    for i in range(len(menu_items)):
        item = menu_items[i]
        item_name = item["name"]
        item_price = float(item["price"])
        item_description = item["description"]
        item_image = item["image"]
        items.append({"item_name":item_name,"item_description":item_description,"item_price":item_price,"item_image":item_image})
    result["menu_items"]= items
    return result
#function compeleted

#given links in data sample_json links
given_links = [
    "https://www.talabat.com/uae/restaurant/621133/ginos-deli-jlt?aid=1308",
    "https://www.talabat.com/uae/restaurant/645430/pasta-della-nona-jlt-jumeirah-lakes-towers?aid=1308",
    "https://www.talabat.com/uae/restaurant/50445/pizzaro-marina-3?aid=1308",
    "https://www.talabat.com/uae/restaurant/605052/the-pasta-guyz-dubai-marina?aid=1308",
    "https://www.talabat.com/uae/restaurant/621796/pizza-di-rocco-jumeirah-lakes-towers--jlt?aid=1308"
]

#5 urls randomly chosen
my_urls = [
'https://www.talabat.com/uae/restaurant/648008/jaffer-bhais-restaurant-al-barsha-1?aid=1308',
'https://www.talabat.com/uae/restaurant/41433/yin-yang-restaurant-jumeriah-lakes-towers--jlt?aid=1308',
'https://www.talabat.com/uae/restaurant/643032/oregano-dubai-media-city-dubai-internet-city--dic?aid=1308',
'https://www.talabat.com/uae/restaurant/603280/carluccios-restaurant-cafe-dubai-marina?aid=1308',
'https://www.talabat.com/uae/restaurant/606838/everyday-roastery-coffee-dubai-marina?aid=1308'
]

#all urls 
links = given_links + my_urls


output = {}
count = 0
for i in links:
    y = webscrape(i)
    output[str(count)] = y
    count += 1
response = json.dumps(output)
print(response)
