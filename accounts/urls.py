from django.urls import path
from .views import SignUp


urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up'),
]