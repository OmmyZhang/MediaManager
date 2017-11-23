from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from accounts import views

factory = APIRequestFactory()

userPath = '/user'
userSignupPath = '/user/signup'
userInfoPath = '/user/'

#WAIT BECAUSE USER STRUCT IS COMPLEX

