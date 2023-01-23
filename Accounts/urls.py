from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup_page, name='sign_up'),
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('take_test/', views.record_response, name='record_res'),
    path("analyze_response/<int:id>", views.analyze_user_response, name="analyze_response"),

    # path('')
]