from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views
from .forms import UserLoginForm
from .views import UserRegisterView

__all__ = ['urlpatterns']

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(
        template_name='users/login.html', authentication_form=UserLoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('profile/<int:pk>', views.UserUpdateView.as_view(), name='profile'),
    path('profile/<int:pk>/password_change', views.PasswordChangeView.as_view()
         , name='password-change'),
    path('login/password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('login/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    re_path(
        'login/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('login/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
]
