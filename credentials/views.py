from django.contrib import auth, messages
from django.http import HttpResponse
from django .contrib.auth.models import User
from django.shortcuts import render, redirect
from  .forms import Addform
from .models import Registration,Branch,District,Account



# Create your views here.

def formpage(request):
    form = Addform()
    if request.method == 'POST':
        form = Addform(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.info(request,"Application Accepted")
            return render(request,"message.html")
    return render(request,'formpage.html',{'form':form})


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('credentials:home')
    return redirect('credentials:login')

def messages_form(request):
    return render("message.html")

def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id= district_id)
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})




def newpage(request):
    return render(request,"newpage.html")

def home(request):
    # return HttpResponse("helloworld")
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = user.id
            return render(request,"newpage.html",{'user':user})
        else:
            messages.info(request,"Invalid User")
            return redirect('credentials:login')
    else:
        return render(request,"login.html")

def register(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if(password==cpassword):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exist")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('credentials:login')

        else:
              messages.info(request, "password not matching")
              return redirect('credentials:register')


    return render(request,"register.html")