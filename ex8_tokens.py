import json
import requests
import time

url_api = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url_api)
response_as_json = json.loads(response.text)
token = response_as_json['token']
delay = response_as_json['seconds']
response_before_done = requests.get(url_api, params={"token": token})
status_before_done = json.loads(response_before_done.text)['status']

if status_before_done == 'Job is NOT ready':
    print('Задача еще не готова, подождите')
else:
    print('Ошибка в статусе когда задача еще не готова')

time.sleep(delay)

response_after_done = requests.get(url_api, params={"token": token})
status_after_done = json.loads(response_after_done.text)['status']
result_after_done = json.loads(response_after_done.text)['result']

if status_after_done == 'Job is ready' and result_after_done is not None:
    print(f"Задача успешно выполнена, 'result': {result_after_done}")
else:
    print('Задача не выполнена, произошла ошибка')
