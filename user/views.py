from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import *

# kullanıcının girişli olması şartı için yapılacak import
from django.contrib.auth.decorators import login_required
# kullanıcı girişi-çıkışı için importlar
from django.contrib.auth import authenticate, login, logout

# Kayıt Olma Fonksiyonu
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Kullanıcı Adı Kullanımda !')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email Kullanımda !')
            elif len(sifre) < 6:
                messages.error(request, 'Şifre En Az 6 Karakter Olmalıdır !')
            elif kullanici.lower() in sifre.lower():
                messages.error(request, 'Kullanıcı Adı ve Şifre Aynı Olmamalıdır')
            else:
                user = User.objects.create_user(
                    username = kullanici,
                    email = email,
                    password = sifre
                )
                user.save()
                messages.success(request,'Kayıt tamamlandı. Giriş Yapabilirsiniz.')
                return redirect('index')
        else:
            messages.error(request,'Şifreler Eşleşmiyor !')
    return render(request,'register.html')

# Kullanıcı Girişi Fonksiyonu
def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request,'Giriş Yapıldı')
            return redirect('profiles')
        else:
            messages.error(request,'Kullanıcı Adı veya Şifre Hatalı')
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')
def profiles(request):
    profiller = Profile.objects.filter(user = request.user)
    context = {
        'profiller':profiller
    }
    return render(request, 'browse.html', context)

@login_required(login_url='login')
def createProfile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if Profile.objects.filter(user = request.user).count() < 4:
                newProfile = form.save(commit=False)
                newProfile.user = request.user
                newProfile.save()
                messages.success(request,'Profil Oluşturuldu')
                return redirect('profiles')
            else:
                messages.warning(request, 'En Fazla 4 Adet Profil Oluşturabilirsiniz')
                return redirect('profiles')
    context = {
        'form':form
    }
    return render(request, 'create-profile.html',context)


