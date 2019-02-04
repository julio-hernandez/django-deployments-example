from django.shortcuts import render
from appbasic.forms import UserForm, UserProfileForm
# authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse THIS IS PYTHON2
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def indexView(request):
    return render(request, 'appbasic/index.html')


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def registrationView(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)  # save user to db
            user.set_password(user.password)  # hash password
            user.save()  # save user to database

            profile = profile_form.save(commit=False)
            profile.basic_user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    data_dict = {'registered': registered, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'appbasic/register.html', context=data_dict)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:  # If user has been authenticated
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed!')
            print("Username: {}  and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'appbasic/login.html')
