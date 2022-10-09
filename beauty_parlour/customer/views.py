from django.shortcuts import render


def customer_home(request):
    return render(request,'customer_template/customerhome.html')

def customer_about(request):
    return render(request,'customer_template/about.html')    

def customer_login(request):
    return render(request,'customer_template/login.html') 

def customer_booking(request):
    return render(request,'customer_template/booking.html')

def customer_services(request):
    return render(request,'customer_template/services.html')

def customer_contact(request):
    return render(request,'customer_template/contact.html')            

def customer_facial(request):
    return render(request,'customer_template/facial.html')    
# Create your views here.