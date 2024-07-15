import requests
import allure
import pytest


class Test_Registration:

    @allure.feature('User Registration')
    @allure.suite('Unsuccessful Registration')
    @allure.title('Test Unsuccessful Registration: Missing Password')
    @pytest.mark.regression

    def test_Rregister_unsuccesful(self):
        body = {
            "email": "Lilit@mail.ru",
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )
        print(response.json())
        with allure.step('Verify status code is 400'):
            assert response.status_code == 400, 'Status code is not correct'

        with allure.step('Verify error in response'):
            assert 'error' in response.json(), 'Response does not contain error'

        with allure.step('Verify error message'):
            assert response.json()['error'] == 'Missing password', 'Error message is not correct'

    @allure.feature('User Registration')
    @allure.suite('Successful Registration')
    @allure.title('Test Successful Registration')
    @pytest.mark.regression

    def test_Rregister_succesful(self):
        body = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )
        print(response.json())
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step('Verify "id" field in response'):
            assert 'id' in response.json(), 'Response does not contain "id"'
            assert response.json()['id'] != '', 'Id is empty'

        with allure.step('Verify "token" field in response'):
            assert 'token' in response.json(), 'Response does not contain "token"'
            assert response.json()['token'] != '', 'Token is empty'