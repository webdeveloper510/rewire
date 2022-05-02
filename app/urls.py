from django.urls import path, include
from app.views import loginview
from app.views import signupview
from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path('', signupview.create, name='signup'),
    # path('signup/', signupview.create, name='signup'),
    path('login',loginview.user_login,name="login"),
    path('logout',loginview.userLogout,name="logout"),
    path('activate/<uidb64>/<token>/',signupview.activate, name='activate'),
    path("password_reset", loginview.password_reset_request, name="password_reset"),
    path("password_complete/<uidb64>/<token>/", loginview.change_password, name="password_complete"), 
    path("policy",signupview.policies,name="policy"),  
    path("data",signupview.make,name="data"),  
    path("update/<int:id>",signupview.update,name="update"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('show', signupview.new, name='show'),
    path('type', signupview.insurance, name='type'),
    path('add', signupview.insurance_add, name='add'),
]
