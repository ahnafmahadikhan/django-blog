from django.urls import path
from .views import home, post_detail, create_post, edit_post, delete_post, signup_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='detail'),
    path('create/', create_post, name='create'),
    path('edit/<int:id>/', edit_post, name='edit'),
    path('delete/<int:id>/', delete_post, name='delete'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
]
