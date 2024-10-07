from django.urls import path

from cat import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-cat/', views.add_cat_view, name='add_cat'),
    path('edit-cat/<int:cat_id>/', views.edit_cat_view, name='edit_cat'),
    path('delete-cat/<int:cat_id>/', views.delete_cat_view, name='delete_cat'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/<int:user_id>/', views.chat_with_user_view, name='chat_with_user'),
]
