import requests
from bs4 import BeautifulSoup
import traceback

MOBILE_PRICE_URL = "https://www.samsung.com/in/smartphones/galaxy-s20/buy/"


def get_price():
    try:
        page = requests.get(MOBILE_PRICE_URL)
        soup = BeautifulSoup(page.text, 'html.parser')
        price_div = soup.find('div', {'class': 'hubble-offer-banner__detail-title'})
        price_txt = price_div.findChild('h2').text
        print(price_txt)
        return int(price_txt.split(' ')[-1].split('*')[0])
    except:
        print('Error occurred when finding price for the mobile')
        traceback.print_exc()
        return -1


if __name__ == '__main__':
    print(get_price())
