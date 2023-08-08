from django.shortcuts import render, redirect
from .models import Header
from .models import Table, Players,Statistics
from .forms import RegisterForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 


# Create your views here.
def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accounts was created for ' + user)
    else:
        form = RegisterForm()
       
    return render(request, 'league/register.html', {'form':form})


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, "Invalid Username or Password")    
    return render(request, 'league/login.html')


def out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    base = Header.objects.all()
    data = Table.objects.all()
    context = { 'base' : base, 
                'data' : data}
    return render(request, 'league/table.html', context )
 
@login_required(login_url='login')
def index(request):
    players =  Players.objects.all()
    context = {'players':players}
    return render(request, 'league/players.html', context)
    
@login_required(login_url='login')  
def stat(request):
    stats = Statistics.objects.all()
    context = {'stats' : stats}
    return render(request, 'league/stat.html',context)