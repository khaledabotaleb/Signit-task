from django.test import TestCase
from user.models import User
# Create your tests here.

import json
import pytest
from rest_framework.test import APIRequestFactory, APIClient

from user.tests.factories import UserFactory
from user.views import CreateUserAPI


@pytest.mark.django_db
class TestUserEndpoints:
    endpoint = '/api/v1/user/'

    def test_create(self, api_client):
        user = UserFactory()
        expected_json = {
            'email': "test@test.com",
            'password': "password@123",
            'full_name': "test username"
        }

        response = api_client().post(
            self.endpoint,
            data=json.dumps(expected_json),
            content_type='application/json'
        )
        assert response.status_code == 201
        assert len(response.data)

    def test_retrieve(self, api_client):
        user = UserFactory()
        url = f'{self.endpoint}{user.id}/'
        response = api_client().get(url)
        assert response.status_code == 200

    def test_update(self, rf, api_client):
        old_user = UserFactory()
        new_user = UserFactory()
        new_dict = {
            'full_name': new_user.full_name
        }
        url = f'{self.endpoint}{old_user.id}/'
        response = api_client().put(
            url,
            new_dict,
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content) == new_dict

    def test_delete(self, api_client):
        user = UserFactory()
        url = f'{self.endpoint}{user.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert User.objects.all().count() == 0
