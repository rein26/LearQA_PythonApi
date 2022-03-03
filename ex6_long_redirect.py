import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(response.history)
redirects = len(response.history)
print(f"Кол-во редиректов: {redirects}")