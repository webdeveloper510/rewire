from django.urls import path
from app.views import loginview
from app.views import signupview



urlpatterns = [
    path('', signupview.index, name='index'),
    path('signup', signupview.create, name='signup'),
    path('activate/<uidb64>/<token>/',signupview.activate, name='activate'),
    path("password_reset", loginview.password_reset_request, name="password_reset"),
    path("password_complete/<uidb64>/<token>/", loginview.change_password, name="password_complete"), 
    
]