import requests
import pytest
import allure

class Test_Users():

    @allure.feature('User API')
    @allure.suite('List Users')
    @allure.title('Test List Users')
    @pytest.mark.regression
    def test_list_users(self):
        response = requests.get('https://reqres.in/api/users')
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step('Verify total count calculation'):
            assert response.json()['per_page'] * response.json()['total_pages'] == response.json()[
                'total'], "The total count of users is incorrect"

        with allure.step('Verify count of users on the page'):
            assert len(response.json()['data']) == 6, "The count of users on the page is incorrect"

        with allure.step('Verify details of each user'):
            for user in response.json()['data']:
                assert 'id' in user, 'Response does not contain "id"'
                assert user['id'] != '', 'Id is empty'
                assert 'email' in user, 'Response does not contain "email"'
                assert user['email'] != '', 'Email is not empty'
                assert 'first_name' in user, 'Response does not contain "first_name"'
                assert 'last_name' in user, 'Response does not contain "last_name"'
                assert 'avatar' in user, 'Response does not contain "avatar"'

        with allure.step('Verify presence of support field'):
            assert 'support' in response.json(), 'Response does not contain "support"'

    @allure.feature('User API')
    @allure.suite('Single User')
    @allure.title('Test Single User')
    @pytest.mark.regression
    def test_single_user(self):
        ID = 2
        response = requests.get(f'https://reqres.in/api/users/{ID}')
        with allure.step(f'Verify status code is 200 for user ID {ID}'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step(f'Verify ID is correct for user ID {ID}'):
            assert response.json()['data']['id'] == ID, 'ID is not correct'

        with allure.step(f'Verify email is not empty for user ID {ID}'):
            assert response.json()['data']['email'] != '', 'Email is not empty'

        with allure.step(f'Verify email format is correct for user ID {ID}'):
            assert response.json()['data']['email'].count('@') == 1, 'Email format is incorrect'

    @allure.feature('User API')
    @allure.suite('Single User')
    @allure.title('Test Single User Not Found')
    @pytest.mark.regression
    def test_single_user_is_not_found(self):
        ID = 13
        response = requests.get(f'https://reqres.in/api/users/{ID}')
        with allure.step(f'Verify status code is 404 for non-existent user ID {ID}'):
            assert response.status_code == 404, 'Status code is not correct'

