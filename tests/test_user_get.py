from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

class TestUserGet(BaseCase):
    @allure.testcase("https://google.com", 'test_case get user details not auth')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        unexpected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response, unexpected_fields)

    @allure.testcase("https://google.com", 'test_case get user details auth as same user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_details_auth_as_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.testcase("https://google.com", 'test_case get details another user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_details_another_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        another_user_id = 28892

        response2 = MyRequests.get(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_has_key(response2, "username")
        unexpected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response2, unexpected_fields)
