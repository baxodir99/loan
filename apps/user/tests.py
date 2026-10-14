from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.test.client import encode_multipart, RequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User


factory = APIRequestFactory()
user = User.objects.get(username='user12345')