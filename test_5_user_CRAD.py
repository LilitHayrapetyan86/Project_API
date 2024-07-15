import requests
import allure
import pytest

class Test_User_CRAD():
    @pytest.fixture()
    def user_id(user_id):
        body = {
        "name": "Lilit",
        "job": "QA"
    }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )
        user_id = response.json()['id']
        print("USER ID", user_id)
        yield user_id
        print("deleting the user")
        print(requests.delete(f'https://reqres.in/api/users/{user_id}').status_code)

    @allure.feature('User Management')
    @allure.suite('Create User')
    @allure.title('Test Create User')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_create_user(user_id):
        body = {
            "name": "Lilit",
            "job": "QA"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )
        user_id = response.json()['id']
        with allure.step('Verify status code is 201'):
            assert response.status_code == 201, 'Status code is not correct'
        with allure.step('Verify name and job'):
            assert response.json()['name'] == 'Lilit', 'Name is not correct'
            assert response.json()['job'] == 'QA', 'Job is not correct'
        with allure.step('Verify ID and createdAt'):
            assert 'id' in response.json(), 'Response does not contain id'
            assert response.json()['id'] != '', 'ID is empty'
            assert 'createdAt' in response.json(), 'Response does not contain "createdAt"'
        requests.delete(f'https://reqres.in/api/users/{user_id}')

    @allure.feature('User Management')
    @allure.suite('Update User')
    @allure.title('Test Update User (PUT)')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_put_user(user_id):
        body = {
            "name": "Lilit_Hayrapetyan",
            "job": "QA_Lead"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            f'https://reqres.in/api/users/{user_id}',
            json=body,
            headers=headers
        )
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'
        with allure.step('Verify updated name and job'):
            assert response.json()['name'] == 'Lilit_Hayrapetyan', 'Name is not correct'
            assert response.json()['job'] == 'QA_Lead', 'Job is not correct'
        with allure.step('Verify updatedAt'):
            assert 'updatedAt' in response.json(), 'Response does not contain "updatedAt"'
            assert response.json()['updatedAt'] != '', 'Updated date is empty'

    @allure.feature('User Management')
    @allure.suite('Update User')
    @allure.title('Test Update User (PATCH)')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_patch_user(user_id):
        body = {
            "name": "Lilit_Hay",
            "job": "QA_CEO"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            f'https://reqres.in/api/users/{user_id}',
            json=body,
            headers=headers
        )
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'
        with allure.step('Verify updated name and job'):
            assert response.json()['name'] == 'Lilit_Hay', 'Name is not correct'
            assert response.json()['job'] == 'QA_CEO', 'Job is not correct'
        with allure.step('Verify updatedAt'):
            assert 'updatedAt' in response.json(), 'Response does not contain "updatedAt"'
            assert response.json()['updatedAt'] != '', 'Updated date is empty'

    @allure.feature('User Management')
    @allure.suite('Delete User')
    @allure.title('Test Delete User')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_delete_user(user_id):
        body = {
            "name": "Lilit",
            "job": "QA"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )
        user_id = response.json()['id']
        response = requests.delete(f'https://reqres.in/api/users/{user_id}')
        with allure.step('Verify status code is 204'):
            assert response.status_code == 204, 'Status code is not correct'

