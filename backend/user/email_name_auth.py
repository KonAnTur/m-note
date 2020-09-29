from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from re import *

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):

        pattern_email = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        is_valid_email = pattern_email.match(username)
        
        if is_valid_email:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        return None