from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.contrib import messages
from app.forms.user import *
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.contrib.auth import  update_session_auth_hash
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model




def index(request):
     return render(request,"index.html")

def create(request):
       
    context=user.objects.all()
    if request.method == 'POST':
        accountform = AddCreateForm(request.POST)
        if accountform.is_valid():
         

            name=request.POST.get("username")
            
            unique_id = get_random_string(length=5)
            uniqueName=name + unique_id
            accountform.username=uniqueName
            print("accountform",accountform.username)    
            new_user = accountform.save(commit=False)
            new_user.is_active = False
            new_user.save()
           


            new_user.entry_code= uniqueName
                
            
            new_user.set_password(
                accountform.cleaned_data.get('password')         
            )
            update_session_auth_hash(request, request.user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('signup/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token':account_activation_token.make_token(new_user),
            })
            to_email = accountform.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, 
                        message, 
                        to=[to_email]
            )
           

            a=accountform.save()
           
            email.send()
            messages.success(request,"Thanks for registering with us.Please confirm your email address to complete the registration.",extra_tags='logout')
            return redirect('signup')
              

        else:
           
            return render(request,"signup/signup.html",{'form':accountform,"context":context})

    form = AddCreateForm()
    return render(request,"data.html",{'form':form,"context":context})


def activate(request, uidb64, token):
    User=get_user_model()
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        users = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        users = None
    if users is not None and account_activation_token.check_token(users, token):
        users.is_active = user.objects.filter(id=uid).update(is_active=True)
        login(request, users)
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')

def policies(request):
    
    show=policy()   
    submitbutton= request.GET.get('text')
    print("show",submitbutton)
    
    show.insurer=request.GET.get("d1")
    show.product=request.GET.get("d2")
    show.policy_number=request.GET.get("d3")
    show.renewal=request.GET.get("d4")
    show.policy_yearly=request.GET.get("d5")
    show.status=request.GET.get("d6")
  
    show.save()
    show=show.insurer
    z=policy.objects.all()
    return render(request,"data.html",{"show":z,'b':1})
    
    
def make(request):
    z=policy.objects.all()
    if request.method == "GET":
        print("entry")
        submitbutton= request.GET.get('check')
        print("showed",submitbutton)
        if not submitbutton:
            submitbutton="dd"
            print("ss",submitbutton)  
    return render(request,"data.html",{"show":z,'submit':submitbutton})
    
    
def update(request,id):
    print("hello")
    submitbutton= request.POST.get('ss')
    print("try",submitbutton)
    ploicies = policy.objects.get(pk=id)
    if request.method == 'POST':
     
        ploicies.insurer = request.POST.get('insurer')
        ploicies.product = request.POST.get('product')
        ploicies.policy_number = request.POST.get('policy_number')
        ploicies.renewal = request.POST.get('renewal')
        ploicies.policy_yearly = request.POST.get('policy_yearly')
        ploicies.status = request.POST.get('status')

        ploicies.save()
        messages.success(request,"Policy details updated Successfully.")
        return redirect("/data")
        
    return render(request,"update.html",{'agencies':ploicies})