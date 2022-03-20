from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format.Response text is '{response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have not ket '{name}"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format.Response text is '{response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have not ket '{name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format.Response text is '{response.text}"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have not ket '{name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format.Response text is '{response.text}"

        assert name not in response_as_dict, f"Response JSON shouldn't have not ket '{name}. But it's present"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format.Response text is '{response.text}"

        for name in names:
            assert name not in response_as_dict, f"Response JSON shouldn't have not key '{name}'. But it's present"

    @staticmethod
    def assert_code_status(response: Response, expecter_status_code):
        assert response.status_code == expecter_status_code, \
            f"Unexpected status code! Expected: {expecter_status_code}. Actual: {response.status_code}"
