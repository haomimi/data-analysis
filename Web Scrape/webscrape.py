import urllib3
import re

urllib3.disable_warnings()
# link to the target webpage
link = 'https://www.amazon.com/dp/B06XY6Z667/ref=dp_cerb_1'
# part of html to locate the price, which could be changing from time to time
pattern = 'priceBlockBuyingPriceString">'

def run_scrape(link,pattern):
    http = urllib3.PoolManager()
    response = http.request('GET', link)
    data_str = str(response.data)
    # locate where the piece is in all 
    idx = re.search(pattern,data_str).span()
    price_chunk = data_str[idx[1]: idx[1]+20]
    price = price_chunk.split('</span')
    print('Price:', price[0])

if __name__ == "__main__":
    run_scrape(link,pattern)