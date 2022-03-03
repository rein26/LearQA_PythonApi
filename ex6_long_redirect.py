import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
url = response.url
redirects = len(response.history)

print(f"Кол-во редиректов: {redirects}")
print(f"Итоговый url {url}")
