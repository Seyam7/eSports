from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import faceitReg
from home.models import eleagueReg

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def registerUser(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

def counterStrike(request):
    return render(request, 'counterStrike.html')

def lol(request):
    return render(request, 'lol.html')

def cod(request):
    return render(request, 'cod.html')

def teams(request):
    return render(request, 'teams.html')

def teams2(request):
    return render(request, 'teams2.html')

def teams3(request):
    return render(request, 'teams3.html')

def players(request):
    return render(request, 'players.html')

def players2(request):
    return render(request, 'players2.html')

def players3(request):
    return render(request, 'players3.html')

def tournaments(request):
    return render(request, 'tournaments.html')

def tournaments2(request):
    return render(request, 'tournaments2.html')

def tournaments3(request):
    return render(request, 'tournaments3.html')

def tournamentsCompleted(request):
    return render(request, 'tournamentsCompleted.html')

def tournamentsCompleted2(request):
    return render(request, 'tournamentsCompleted2.html')

def tournamentsCompleted3(request):
    return render(request, 'tournamentsCompleted3.html')

def upcomingTournaments(request):
    return render(request, 'upcomingTournaments.html')

def upcomingTournaments2(request):
    return render(request, 'upcomingTournaments2.html')

def upcomingTournaments3(request):
    return render(request, 'upcomingTournaments3.html')

def faceit(request):
    if request.method == "POST":
        pname = request.POST.get('pname')
        tname = request.POST.get('tname')
        femail = request.POST.get('femail')
        faceit = faceitReg(pname=pname, tname=tname, femail=femail, date = datetime.today())
        faceit.save()
        messages.success(request, 'Your registration is successful!')
    return render(request, 'faceit.html')

def eleague(request):
    if request.method == "POST":
        epname = request.POST.get('epname')
        etname = request.POST.get('etname')
        efemail = request.POST.get('efemail')
        eleague = eleagueReg(epname=epname, etname=etname, efemail=efemail, date = datetime.today())
        eleague.save()
        messages.success(request, 'Your registration is successful!')
    return render(request, 'eleague.html')

def faceit2(request):
    faceit2 = faceitReg.objects.all()
    return render(request, 'faceit2.html',
    {'faceit2':faceit2})

def eleague2(request):
    eleague2 = eleagueReg.objects.all()
    return render(request, 'eleague2.html',
    {'eleague2':eleague2})

def dreamhack(request):
    return render(request, 'dreamhack.html')

def esl(request):
    return render(request, 'esl.html')