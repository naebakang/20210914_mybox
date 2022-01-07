import requests
from bs4 import BeautifulSoup
from datetime import datetime

latencies = []


def get_currency_exchange_rate(pair1, pair2):
    print("-----currency pair-----")
    print(pair1, 'and', pair2)
    print("-----------------------")
    ex_datetime = datetime.now()
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    while True:
        response = requests.get("https://kr.investing.com/currencies/{}-{}".format(pair1, pair2), headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find('span', {'id': 'last_last'})
        latencies.append(datetime.now().timestamp() - ex_datetime.timestamp())
        print(datetime.now(), containers.text)
        ex_datetime = datetime.now()


if __name__ == '__main__':
    try:
        get_currency_exchange_rate('usd', 'krw')
    except KeyboardInterrupt:
        print('stop')
        print('latencies mean is:', sum(latencies) / len(latencies))
