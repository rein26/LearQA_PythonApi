import requests

class TestCookie:
    def setup(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        self.response = requests.get(url)

    def test_cookie(self):
        actual_cookies = self.response.cookies.get("HomeWork")
        expected_cookies = "hw_value"
        assert self.response.status_code == 200, "Status code is not equal 200"
        assert actual_cookies == expected_cookies, "Cookies are invalid"
