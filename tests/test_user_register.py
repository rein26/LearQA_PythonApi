import pytest
import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    fields_in_json = [
        ('password'),
        ('username'),
        ('firstName'),
        ('lastName'),
        ('email'),
    ]

    @allure.testcase("https://google.com", 'test_case create user successfully')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.testcase("https://google.com", 'test_case create user with existing email')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    @allure.testcase("https://google.com", 'test_case create user incorrect email')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post('/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == 'Invalid email format', \
            f"Email {email} is in invalid format"

    @allure.testcase("https://google.com", 'test_case cteate user without field')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('field', fields_in_json)
    def test_create_user_without_field(self, field):
        data = self.prepare_registration_data()
        del data[field]
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        response_decode = response.content.decode("utf-8")
        assert response_decode == f"The following required params are missed: {field}", \
            f"Error in returned content. Response content: {response.text}"

    @allure.testcase("https://google.com", 'test_case cteate user short name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_short_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = 'l'
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == "The value of 'firstName' field is too short", \
            f"Error in returned content. Response content: {response.text}"

    @allure.testcase("https://google.com", 'test_case cteate user long name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_long_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = 'l' * 251
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == "The value of 'firstName' field is too long", \
            f"Error in returned content. Response content: {response.text}"
