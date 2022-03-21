from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def setup(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response, "id")
        self.new_name = "Changed Name"

    def test_edit_just_created(self):
        #LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        #EDIT
        response2 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": self.new_name}
        )

        Assertions.assert_code_status(response2, 200)

        #GET
        response3 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response3,
            "firstName",
            self.new_name,
            "Wrong name of the user after edit"
        )

    def test_edit_without_auth(self):
        response2 = MyRequests.put(
            f"/user/{self.user_id}",
            data={"firstName": self.new_name}
        )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_content(
            response2,
            response2.text,
            "Auth token not supplied"
        )


    def test_edit_with_another_auth(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # EDIT
        response2 = MyRequests.put(
            f"/user/29089",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": '12345'}
        )

        Assertions.assert_code_status(response2, 400)

    def test_edit_invalid_email(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # EDIT
        response2 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": 'learnqaexample.com'}
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_content(
            response2,
            response2.text,
            "Invalid email format"
        )

    def test_edit_short_name(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # EDIT
        response2 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": 'l'}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "error",
            "Too short value for field firstName",
            f"Error in returned content. Response content: {response2.text}"
        )

