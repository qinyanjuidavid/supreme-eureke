from django.contrib.auth import views as auth_views
from django.urls import path
from modules.accounts import views
from modules.accounts.views import SignupView

app_name = "accounts"

urlpatterns = [
    # path(
    #     "login/",
    #     auth_views.LogoutView.as_view(
    #         template_name="accounts/login.html",
    #     ),
    #     name="login",
    # ),
    path("", views.loginView, name="login"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="accounts/logout.html",
        ),
        name="logout",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            success_url="/accounts/password_reset/done/",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/reset/done/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("home/", views.HomeView, name="home"),
]
