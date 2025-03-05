from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import RegisterView, MyLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
