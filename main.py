from bottle import route, run, request, template
from datetime import datetime

# 最新の数値と受信時間を保存するリスト
latest_numbers = []
congestion_levels = []

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
    global congestion_levels
    latest_date = datetime.now().strftime("%Y-%m-%d") if latest_numbers else "データなし"
    
    # 平均距離と背景色、混雑度を計算
    if latest_numbers:
        average_distance = sum(distance for distance, _ in latest_numbers) / len(latest_numbers)
        congestion_level_value = round(average_distance * 100 / 1000, 1)
        congestion_level = f"{congestion_level_value}"
        congestion_levels.append([congestion_level, latest_date])
        
    else:
        congestion_level = "データなし"

    if len(congestion_levels) > 10:
        congestion_levels = congestion_levels[-10:]

    return template('template.html', numbers=latest_numbers, latest_date=latest_date, congestion_level=congestion_level, congestion_levels=congestion_levels)

run(host="localhost", port=8080, debug=True)
