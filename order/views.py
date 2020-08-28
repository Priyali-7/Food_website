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

def register(request):
    if request.method == 'POST':
        full_name=request.POST['full_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1== password2:
            if UserRegister.objects.filter(user_name=user_name).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif UserRegister.objects.filter(email=email).exists():
                messages.info(request, 'Email Id taken')
                return redirect('register')
            else:
                user= UserRegister(full_name = full_name, user_name= user_name, email=email, password1=password1)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')    
        return redirect('/')
        
    else:
         return render(request, 'order/register.html')


def login(request):
    if request.method== "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user= auth.authenticate(user_name= user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid user')
            return redirect('login')

    else:
        return render(request, 'order/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')
