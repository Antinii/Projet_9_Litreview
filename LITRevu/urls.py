"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
        name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
        name='password_change_done'),
    path('home/', blog.views.home, name='home'),
    path('blog/create_ticket/', blog.views.create_ticket, name='create_ticket'),
    path('blog/<int:ticket_id>/edit_ticket', blog.views.edit_ticket, name='edit_ticket'),
    path('create_review/<int:ticket_id>/', blog.views.create_review, name='create_review'),
    path('blog/<int:review_id>/edit_review/', blog.views.edit_review, name="edit_review"),
    path('blog/create_ticket_and_review/', blog.views.create_ticket_and_review, name='create_ticket_and_review'),
    path('follow_user', blog.views.follow_user, name='follow_user'),
    path('unfollow', blog.views.unfollow, name='unfollow'),
    path('my_posts/', blog.views.my_posts, name="my_posts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
