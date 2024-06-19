from django.shortcuts import render,redirect
from . models import Contact
from django.conf import settings as conf_settings
from django.contrib import messages #import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def home(request):
    return render(request,'webapp/home.html')

  

def rebate(request):
    if request.method == 'POST':
        serive_list = []
        name = request.POST.get("name")
        email_skype = request.POST.get("email")
        countrycode = request.POST.get("countryCode")
        mobile_no = request.POST.get("mobile_no")
        service =  request.POST.getlist("select_service")
        broker  = request.POST.getlist("select_broker")
        serive_list.append(service)
        msg = request.POST.get("msg")
        contact = Contact(name=name,email_skype=email_skype,mobile_no=mobile_no,country_code=countrycode,service=service,broker=broker,msg=msg)
        contact.save()  
        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = email_skype
        bcc_email = 'phanikanth8143385760@gmail.com'
      
        text_content = render_to_string('{0}/templates/webapp/mail.html'.format(conf_settings.BASE_DIR), {'name':name, 'email':mail_to, 
                                                    'phone_no':mobile_no,'service':service,'broker':broker})
        msg = EmailMultiAlternatives("WELCOME TO FX", text_content, mail_from, [mail_to], bcc=[bcc_email])
        msg.attach_alternative(text_content, 'text/html')
        msg.send()
        return redirect('web_home')
    return render(request,'webapp/rebate.html') 

def demat(request):
    return render(request,'webapp/demat.html')       

def forex(request):
    return render(request,'webapp/forex.html') 

def payment_getway(request):
    return render(request,'webapp/payment_getway.html') 

def six_info(request):
    return render(request,'webapp/6i_info.html')


def bdswiss_info(request):
    return render(request,'webapp/bdswiss_info.html')   

def fxtm_info(request):
    return render(request,'webapp/fxtm_info.html') 

def royal_info(request):
    return render(request,'webapp/royal_info.html')  

def swiss_markets_info(request):
    return render(request,'webapp/swiss_markets_info.html')

def tio_markets_info(request):
    return render(request,'webapp/tiomarket_info.html')

def easy_market_info(request):
    return render(request,'webapp/easy_market_info.html') 

def hot_forex_info(request):
    return render(request,'webapp/hot_forex_info.html')

def fxpro_info(request):
    return render(request,'webapp/fxpro_info.html') 

def awatrade_info(request):
    return render(request,'webapp/awatrade_info.html')

def pepperstone_info(request):
    return render(request,'webapp/pepperstone_info.html')

def fpmarket_info(request):
    return render(request,'webapp/fpmarket_info.html')

def orbex_info(request):
    return render(request,'webapp/orbex_info.html')

def fxprimus_info(request):
    return render(request,'webapp/fx_primus_info.html')  









    

