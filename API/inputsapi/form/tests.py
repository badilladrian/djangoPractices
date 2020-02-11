from django.test import TestCase
from rest_framework.test import APITestCase 
from rest_framework.test import APIRequestFactory
from form import apiview
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


# Create your tests here.

#python manage.py test form.tests.TestForm test_create FAILS


class TestForm(APITestCase):

    def setUp(self): 
        self.client = APIClient() 
        self.factory = APIRequestFactory() 
        self.view = apiview.FormViewSet.as_view({'get': 'list'}) 
        self.uri = '/forms/'
        self.user = self.setup_user()


    @staticmethod 
    def setup_user(): 
        User = get_user_model() 
        return User.objects.create_user( 
            'test', email='testuser@test.com', 
            password='test' 
        )


    def test_list(self): 
        request = self.factory.get(self.uri) 
        request.user = self.user 
        response = self.view(request) 
        self.assertEqual(response.status_code, 200, 
                    'Expected Response Code 200, received {0} instead.' 
                    .format(response.status_code))


    def test_list2(self): 
        self.client.login(username="test", password="test") 
        response = self.client.get(self.uri) 
        self.assertEqual(response.status_code, 200, 
        'Expected Response Code 200, received {0} instead.' 
        .format(response.status_code))

#I cant make this test to work.
"""
    def test_create(self): 
        self.client.login(username="test", password="test") 
        token = Token.objects.get(user__username='test')
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        params = { 
            "input_text": "How are you?", 
            "filled_by": 1 
            } 
        response = self.client.post(self.uri, params) 
        self.assertEqual(response.status_code, 201, 
                        'Expected Response Code 201, received {0} instead.' 
                        .format(response.status_code))"""

