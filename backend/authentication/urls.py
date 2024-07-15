
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_view, name='root'), 
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('item_list/', views.user_logout, name='web_item_list'),
    path('social-auth/', include('social_django.urls',namespace='social')),
    
]

