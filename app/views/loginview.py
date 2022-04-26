from django.shortcuts import render
from app.models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.hashers import make_password



def user_login(request):
    
  
    if request.method == "POST":
        uname= request.POST.get('uname')
        print(uname)
        upass= request.POST.get('psw')
        print(upass)
       
        
        if request.method == "POST":
          
          current_user = request.user.id

        user = authenticate(username=uname,password=upass)

        if user is not None:
          login(request,user)
          messages.success(request,"You are Successfully LoggedIn")
          return redirect('/')
         
        else:
          messages.error(request,"Invalid Credential", extra_tags='login')
          return redirect('login')
              
    return render(request,"login.html")


  


def password_reset_request(request):
  if request.method == "POST":
    password_reset_form = PasswordResetForm(request.POST)
    if password_reset_form.is_valid():
      data = password_reset_form.cleaned_data['email']
      associated_users = user.objects.filter(Q(email=data))
      if associated_users.exists():
        for userd in associated_users:
          subject = "Password Reset Requested"
          email_template_name = "signup/password_reset_email.txt"
          c = {
          "email":userd.email,
          'domain':'184.168.122.169',
          'site_name': 'Website',
          "uid": urlsafe_base64_encode(force_bytes(userd.pk)),
          "user": userd,
          'token': default_token_generator.make_token(userd),
          'protocol': 'http',
          }
          email = render_to_string(email_template_name, c)
          try:
            send_mail(subject, email, 'test12041966@gmail.com' , [userd.email], fail_silently=False)
          except BadHeaderError:
            return HttpResponse('Invalid header found.')
          return redirect ("/password_reset/done/")
  password_reset_form = PasswordResetForm()
  return render(request,"signup/forget.html", context={"password_reset_form":password_reset_form})



def change_password(request,**kwargs):
  if request.method == "POST":
    show=request.POST.get("password")
    conf = request.POST.get("confirm")
    if show == conf:
      up=make_password(conf)
    
      z=user.objects.update(password=up)
      return redirect("password_reset_complete")
    else:
        messages.success(request,"New Password and Confirm Password must be same")
  return render(request,"signup/password_reset_confirm.html")


def userLogout(request):
  auth.logout(request)
  return redirect('/')