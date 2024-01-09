from bottle import route, run, request, template
from datetime import datetime

# 最新の数値と受信時間を保存するリスト
latest_numbers = []

# 数値を追加するエンドポイント
@route('/add', method='POST')
def add_number():
    number = request.forms.get('number')
    if number:
        latest_numbers.append((int(number), datetime.now().strftime("%H:%M:%S")))
        if len(latest_numbers) > 10:
            latest_numbers.pop(0)
    return "Number added"

# 数値を表示するエンドポイント
@route('/numbers')
def show_numbers():
    latest_date = datetime.now().strftime("%Y-%m-%d") if latest_numbers else "データなし"
    return template('template.html', numbers=latest_numbers, latest_date=latest_date)

run(host="0.0.0.0", port=8080, debug=True)
