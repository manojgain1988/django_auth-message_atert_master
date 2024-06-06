from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib import messages
from .models import contactModel


# Create your views here.
def HomeView(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        city=request.POST['city']

        if contactModel.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exist')
            return redirect('home')
        else:
            data= contactModel.objects.create(name=name,email=email,contact=contact,city=city)
            data.save()
            messages.success(request, 'Successfully Your Submited !')
            return redirect('home')
    return render(request,'home.html')