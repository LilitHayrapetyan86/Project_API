import requests
import allure
import pytest

class Test_delayed():
    @allure.feature('User API')
    @allure.suite('Delayed Response')
    @allure.title('Test Delayed Response')
    @pytest.mark.regression
    def test_delayed_response(self):
        response = requests.get('https://reqres.in/api/users?delay=50')
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step('Verify total count calculation'):
            assert response.json()['total'] == response.json()['total'] // response.json()['per_page'] * \
                   response.json()['per_page'] + response.json()['total'] % response.json()[
                       'per_page'], "The total count of users is incorrect"

        with allure.step('Verify count of users on the page'):
            assert len(response.json()['data']) <= response.json()[
                'per_page'], "The count of users on the page is incorrect"

        with allure.step('Verify details of each user'):
            for user in response.json()['data']:
                assert 'id' in user, 'Response does not contain "id"'
                assert 'email' in user, 'Response does not contain "email"'
                assert user['email'] != '', 'Email is not empty'
                assert 'first_name' in user, 'Response does not contain "first_name"'
                assert 'last_name' in user, 'Response does not contain "last_name"'
                assert 'avatar' in user, 'Response does not contain "avatar"'
