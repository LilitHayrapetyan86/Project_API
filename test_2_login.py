import requests
import allure
import pytest


class Test_Login:

    @allure.feature('User Login')
    @allure.suite('Unsuccessful Login')
    @allure.title('Test Unsuccessful Login: Missing Password')
    @pytest.mark.regression
    def test_login_unsuccessful(self):
        body = {
            "email": "Lilit@mail.ru",
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/login',
            json=body,
            headers=headers
        )
        print(response.json())
        with allure.step('Verify status code is 400'):
            assert response.status_code == 400, 'Status code is not correct'

        with allure.step('Verify "error" field in response'):
            assert 'error' in response.json(), 'Response does not contain error'

        with allure.step('Verify error message'):
            assert response.json()['error'] == 'Missing password', 'Error message is not correct'

    @allure.feature('User Login')
    @allure.suite('Successful Login')
    @allure.title('Test Successful Login')
    @pytest.mark.regression
    def test_login_successful(self):
        body = {
             "email": "eve.holt@reqres.in",
             "password": "cityslicka"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/login',
            json=body,
            headers=headers
        )
        print(response.json())
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step('Verify "token" field in response'):
            assert 'token' in response.json(), 'Response does not contain "token"'

        with allure.step('Verify token is not empty'):
            assert response.json()['token'] != '', 'Token is empty'