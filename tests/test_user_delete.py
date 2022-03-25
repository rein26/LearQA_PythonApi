from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

class TestUserDelete(BaseCase):
    @allure.testcase("https://google.com", 'test_case user delete')
    @allure.severity(allure.severity_level.NORMAL)
    def test_super_user_delete(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        # LOGIN
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        #DELETE
        response2 = MyRequests.delete(
            "/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_content(
            response2,
            response2.text,
            "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        )

    @allure.testcase("https://google.com", 'test_case user delete success')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_delete_success(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 200)

        # GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 404)
        Assertions.assert_response_content(
            response3,
            response3.text,
            "User not found"
        )

    @allure.testcase("https://google.com", 'test_case another user delete')
    @allure.severity(allure.severity_level.MINOR)
    def test_another_user_delete(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/12312",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
