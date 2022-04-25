import requests # отправляет запросы на сайты
import json
from flask import Flask

#import Flask
# Мы хотим получить ответ от сайта
text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

#print(text)

currency = json.loads(text)
#print(currency)
#print('Валюты')
#print(currency['Valute'])

#for cur in currency['Valute']:
#    print(cur)

# Flask для вывода данных на веб-страницу
app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!"
    #return '<h1>Hello world!</h1>'


    # Получаем данные о курсах валют с сайта
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    # Приводим их в нужный вид
    currency = json.loads(text)
    result = ''
    for cur in currency['Valute']:
        result += str(cur) + '<br>'   # в конце добавляем перенос строки
    return result


if __name__ == "__main__":
    app.run()
