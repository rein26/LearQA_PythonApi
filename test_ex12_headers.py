import requests

class TestHeaders:
    def setup(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        self.response = requests.get(url)
        self.header_name = "x-secret-homework-header"

    def test_headers(self):
        expected_headers = "Some secret value"
        actual_headers = self.response.headers.get(self.header_name)
        assert self.response.status_code == 200, "Status code is not equal 200"
        assert actual_headers == expected_headers, "Headers are invalid"