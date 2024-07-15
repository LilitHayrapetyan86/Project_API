import requests
import allure
import pytest


class Test_Resource():


    @allure.feature('Resource API')
    @allure.suite('List Resource')
    @allure.title('Test List Resource')
    @pytest.mark.regression
    def test_list_resource(self):
        response = requests.get('https://reqres.in/api/unknown')
        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step('Verify total count calculation'):
            assert response.json()['total'] == response.json()['total'] // response.json()['per_page'] * \
                   response.json()['per_page'] + response.json()['total'] % response.json()[
                       'per_page'], 'The total count of resources is incorrect'

        with allure.step('Verify presence of data field'):
            assert 'data' in response.json(), 'Response does not contain data'

        with allure.step('Verify count of resources on the page'):
            assert len(response.json()['data']) <= response.json()[
                'per_page'], 'The count of resources on the page is incorrect'

        with allure.step('Verify details of each resource'):
            for resource in response.json()['data']:
                assert 'id' in resource, 'Response does not contain "id"'
                assert 'name' in resource, 'Response does not contain "name"'
                assert 'year' in resource, 'Response does not contain "year"'
                assert 'color' in resource, 'Response does not contain "color"'
                assert 'pantone_value' in resource, 'Response does not contain "pantone_value"'

        with allure.step('Verify presence of support field'):
            assert 'support' in response.json(), 'Response does not contain "support"'

    @allure.feature('Resource API')
    @allure.suite('Single Resource')
    @allure.title('Test Single Resource')
    @pytest.mark.regression
    def test_single_resource(self):
        ID = 8
        response = requests.get(f'https://reqres.in/api/unknown/{ID}')
        #print(response)
        with allure.step(f'Verify status code is 200 for resource ID {ID}'):
            assert response.status_code == 200, 'Status code is not correct'

        with allure.step(f'Verify ID is correct for resource ID {ID}'):
            assert response.json()['data']['id'] == ID, 'ID is not correct'

        with allure.step(f'Verify name is not empty for resource ID {ID}'):
            assert response.json()['data']['name'] != '', 'Name is empty'

    @allure.feature('Resource API')
    @allure.suite('Single Resource')
    @allure.title('Test Single Resource Not Found')
    @pytest.mark.regression
    def test_single_resource_is_not_found(self):
        ID = 23
        response = requests.get(f'https://reqres.in/api/unknown/{ID}')
        with allure.step(f'Verify status code is 404 for non-existent resource ID {ID}'):
            assert response.status_code == 404, 'Status code is not correct'

