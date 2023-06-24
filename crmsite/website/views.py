from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.

    
def home(request):
    records = Record.objects.all()
    username = request.user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'✅ successfully logged In as --> {username} ')
            return redirect('home')
            
        else:
            messages.success(request,"❌ ERROR ! can't login , try again !")
            return redirect('home')
    else: 
        return render(request,'home.html',{'records':records})

def logout_user(request):
    username = request.user
    logout(request)
    messages.success(request,f'✅ {username} has been logged out successfully !')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login the user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username,password=password)
            # login(request,user)
            messages.success(request,"✅ You have been Registered successfully !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})
from django.contrib.auth.models import User
def customer_record(request,pk):
    #If request of user is authenticated
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
       
        return render(request,"record.html",{"customer_record":customer_record})
    else:
        messages.success(request,'❌ You must be logged in to view that page ...')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        object = Record.objects.get(id=pk)
        object.delete()
        messages.success(request,"✅ Record is Deleted Successfully !")
        return redirect('home')
    else:
        username = request.user
        messages.success(request,f"❌ {username} must be logged In !")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"🌐 Record Added !")
                return redirect('home')
            
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"❌ You must be logged in .. ")
        return redirect('home')