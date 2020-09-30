from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Notes

class NotesTestCase(APITestCase):

    def test_note_list(self):
        response_post_not_auth = self.client.post('/api/notes/',
                                   {
                                       "title": "Test1",
                                       "body": '{"time":1554508385558,"blocks":[],"version":"2.12.3"}',
                                   })
        self.assertEqual(response_post_not_auth.status_code, 401)

        response_get_not_auth = self.client.get('/api/notes/')
        self.assertEqual(response_get_not_auth.status_code, 401)

        user = User(
            email='email@gmail.com',
            username='username'
        )
        user.set_password('password')
        user.save()
        Token.objects.create(user=user)
        token = Token.objects.get(user__username='username')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token.key))

        Notes.objects.create(title='test_title_1', body='test_body_1', author=user)
        Notes.objects.create(title='test_title_2', body='test_body_2', author=user)
        Notes.objects.create(title='test_title_2', body='test_body_2', author=user)

        
        response_get_auth = self.client.get('/api/notes/')
        self.assertEqual(response_get_auth.status_code, 200)
        self.assertEqual(len(response_get_auth.data), 3)
        
        response_post_auth = self.client.post('/api/notes/',
                                                {
                                                    "title": "test_title_4",
                                                    "body": "test_body_4"
                                                },
                                                format='json'
                                            )
        response_get_auth = self.client.get('/api/notes/')
        self.assertEqual(len(response_get_auth.data), 4)

    def test_note_detail(self):
        user = User(
            email='email@gmail.com',
            username='username'
        )
        user.set_password('password')
        user.save()
        Token.objects.create(user=user)
        token = Token.objects.get(user__username='username')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token.key))

        Notes.objects.create(title='test_title_1', body='test_body_1', author=user)

        response_get_auth = self.client.get('/api/notes/1/')
        self.assertEqual(response_get_auth.status_code, 200)
        self.assertEqual(response_get_auth.data['id'], 1)

        response_put_auth = self.client.put('/api/notes/1/', {"title": "test_edit_title_1"}, format='json')
        self.assertEqual(response_put_auth.data['title'], "test_edit_title_1")
        self.assertEqual(response_put_auth.status_code, 200)

        response_delete_auth = self.client.delete('/api/notes/1/')
        self.assertEqual(response_delete_auth.status_code, 204)
        response_get_auth = self.client.get('/api/notes/1/')
        self.assertEqual(response_get_auth.status_code, 404)

