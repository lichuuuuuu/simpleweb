import requests
import random
import time

# Bottleサーバーのアドレス
url = 'http://localhost:8080/add'

while True:
    # ランダムな数字を生成
    number = random.randint(1, 1000)

    # POSTリクエストで数字を送信
    try:
        response = requests.post(url, data={'number': number})
        print(f"Sent {number}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    # 1秒待機
    time.sleep(1)
