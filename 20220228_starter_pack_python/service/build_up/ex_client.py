# File encoding: utf8

import requests
import json

BASE = "http://127.0.0.1:5000"


def post_data_to_api(api_key=None):
    """
    POST 요청을 통해 서버에 데이터를 보내고 응답을 받습니다.
    """
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'X-API-Key': api_key,
    }

    print(f"\nPOST 요청 시도 (API Key: {api_key if api_key else '없음'})")
    try:
        # response = requests.post(url=f"{BASE}/restapi/management/request_tr", headers=headers)
        # data_to_send = {
        #     "data_name": "detail_candlestick",
        #     "list_param_key": ["BTCUSDT", "5m"]
        # }
        # response = requests.post(
        #     url=f"{BASE}/restapi/binance/market",
        #     data=json.dumps(data_to_send),
        #     headers=headers
        # )
        # data_to_send = {
        #     "data_name": "detail_balance",
        #     "list_param_key": []
        # }
        # response = requests.post(
        #     url=f"{BASE}/restapi/binance/account",
        #     data=json.dumps(data_to_send),
        #     headers=headers
        # )
        # data_to_send = {
        #     "list_param_key": ["BTCUSDT", 2]
        # }
        # response = requests.put(
        #     url=f"{BASE}/restapi/binance/account/leverage",
        #     data=json.dumps(data_to_send),
        #     headers=headers
        # )
        data_to_send = {
            "dic_order": {
                "side": "sell",
                "direction": "long",
                "symbol": "BTCUSDT",
                "quantity": 0.022,
            }
        }
        response = requests.put(
            url=f"{BASE}/restapi/binance/account/order",
            data=json.dumps(data_to_send),
            headers=headers
        )
        # data_to_send = {
        #     "list_param_key": ["subject", "contents"]
        # }
        # response = requests.put(
        #     url=f"{BASE}/restapi/gmail",
        #     data=json.dumps(data_to_send),
        #     headers=headers
        # )
        # response = requests.post(
        #     url=f"{BASE}/restapi/tistory",
        #     headers=headers
        # )
        response.raise_for_status()
        data = response.json()
        print(f"성공적인 POST 요청 응답: {data}")
    except requests.exceptions.HTTPError as e:
        print(f"POST 요청 실패 (HTTP Error): {e.response.status_code} - {e.response.json().get('error', '알 수 없는 오류')}")
    except requests.exceptions.RequestException as e:
        print(f"POST 요청 중 오류 발생: {e}")


def test_post():
    print("POST:")
    r = requests.post(BASE + "/", json={"title": "New Book", "author": "Tester"})
    print(r.status_code, r.json())

def test_get_all():
    print("\nGET ALL:")
    r = requests.get(BASE + "/")
    print(r.status_code, r.json())

def test_get_one(book_id):
    print(f"\nGET ONE (id={book_id}):")
    r = requests.get(f"{BASE}/{book_id}")
    print(r.status_code, r.json())

def test_put(book_id):
    print(f"\nPUT (id={book_id}):")
    r = requests.put(f"{BASE}/{book_id}", json={"title": "Updated Book", "author": "New Author"})
    print(r.status_code, r.json())

def test_delete(book_id):
    print(f"\nDELETE (id={book_id}):")
    r = requests.delete(f"{BASE}/{book_id}")
    print(r.status_code, r.json())


if __name__ == "__main__":
    # post_data_to_api('dev')
    post_data_to_api('test1234')
