from django.shortcuts import render,redirect
from .models import *
from cars.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_cars=car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=car.objects.order_by('-created_date')
    model_search=car.objects.values_list('model',flat=True).distinct
    city_search=car.objects.values_list('city',flat=True).distinct
    year_search=car.objects.values_list('year',flat=True).distinct
    body_style_search=car.objects.values_list('body_style',flat=True).distinct
    data={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        
        email_subject='You have email from carzone website regarding ' +subject
        message_body='Name ' +name+ ' Email ' +email+ ' phone ' +phone+ ' message ' +message
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'ssivapriya1014@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,'Thank You for contacting us. We will get to you shortly.')
        return redirect('contact')
    
    return render(request,'pages/contact.html')
