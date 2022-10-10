from django.urls import path
from .views import sign_up, verify_login_phone


urlpatterns = [



    path('signup/', sign_up, name='signup'),

    path('verify/', verify_login_phone, name='verify'),
]
