from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import ContactData
# Create your views here.
def home(request):
    return render(request, 'order/home.html')

def services(request):
    return render(request, 'order/services.html')

def contact(request):
    return render(request, 'order/contact.html')

def menu(request):
    return render(request, 'order/menu.html')

def contact_form(request):
    # fetching parameter
    name = request.POST['full_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    comments = request.POST['comment']

    # save to database
    new_record = ContactData(name = name, email = email, phone_number = phone_number, comments = comments)
    new_record.save()

    return HttpResponse('Thankyou , for your feedback!!')
