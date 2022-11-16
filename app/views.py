from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import SignUpForm,Contact,Dashboardform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Dashboard
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def signup(request):
    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():

            fm.save()
            messages.success(request, 'account created successfully')
            send_mail(
                'Testing Mail',
                'Here is the message.',
                'mani.mallula@gmail.com',
                ['vadeppa1994@gmail.com'],
                fail_silently=False,
            )

    else:
        fm=SignUpForm()

    return render(request,'signup.html',{'form':fm})



def ulogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
       return HttpResponseRedirect('/dashboard/')






def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        fm = Contact(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thanks for Contacting Us')
            return HttpResponseRedirect("<h1> Succussfully </h1>")

    else:
        fm = Contact()
    return render(request,'contact.html',{'form':fm})


def home(request):
    blogs = Dashboard.objects.all()
    return render(request, 'home.html', {'blog': blogs,'name':request.user})


@login_required(login_url='/login')
def dashboard(request):
    if request.method == 'POST':

        fm=Dashboardform(request.POST)

        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    fm=Dashboardform()

    return render(request, 'dashboard.html',{'form':fm})




def ulogout(request):
  logout(request)
  return HttpResponseRedirect('/login/')


def deleteb(request,id):
    fm=Dashboard.objects.get(pk=id)
    fm.delete()
    return HttpResponseRedirect('/')

def editb(request, id):
    fm = Dashboard.objects.get(pk=id)
    form = Dashboardform(instance=fm)
    if request.method == 'POST':
        form = Dashboardform(request.POST, instance=fm)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'edit.html', {'form': form})


# def setcookie(request):
#     response = render(request, 'set.html')
#     response.set_cookie('name','ojas',max_age=12)
#     #response.set_cookie('lname', 'Jha', expires=datetime.utcnow()+timedelta(days=2))
#     return response
#
# def getcookie(request):
#     name = request.COOKIES.get('name', "Guest")
#     return render(request, 'get.html', {'name':name})
#
# def delcookie(request):
#     reponse = render(request, 'del.html')
#     reponse.delete_cookie('name')
#     return reponse






# def setsession(request):
#     request.session['name']='ojas'
#     request.session['sname'] = "innovative"
#     return render(request,'sets.html')
#
#
# def getsession(request):
#     name = request.session.get('name')
#     keys = request.session.keys()
#     items = request.session.items()
#     return render(request,'gets.html',{'name':name,'keys':keys,"items":items})
#
#
# def delsession(request):
#     request.session.flush()
#     return HttpResponse('<h1> session got deleted </h1>')

# def middleware(request):
#     return HttpResponse("view line")

