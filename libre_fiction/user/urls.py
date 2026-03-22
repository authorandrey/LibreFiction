from django.urls import path, include
from user.views import RegisterCreateView, LoginView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
