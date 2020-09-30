from django.test import TestCase

from rest_framework.authtoken.models import Token

class UsersTestCase(TestCase):

    def test_registration_and_authorization(self):
        response_reg = self.client.post('/api/users/registration/',
                                   {
                                       "username": "Ivan",
                                       "email": "ivan@gmail.com",
                                       "password": "152566"
                                   })
        self.assertEqual(response_reg.status_code, 201)
        self.assertEqual(response_reg.data, {'username': 'Ivan', 'email': 'ivan@gmail.com'})

        token = Token.objects.get(user__username=response_reg.data['username'])
        response_auth = self.client.post('/api/users/authorization/',
                                   {
                                       "username": "Ivan",
                                       "password": "152566"
                                   },
                                   format='json')
        self.assertEqual(response_auth.status_code, 200)
        self.assertEqual(response_auth.data["token"], token.key)
        self.assertEqual(response_auth.data["username"], "Ivan")

        token = Token.objects.get(user__username=response_reg.data['username'])
        response_auth = self.client.post('/api/users/authorization/',
                                   {
                                       "username": "ivan@gmail.com",
                                       "password": "152566"
                                   },
                                   format='json')
        self.assertEqual(response_auth.status_code, 200)
        self.assertEqual(response_auth.data["token"], token.key)
        self.assertEqual(response_auth.data["username"], "Ivan")