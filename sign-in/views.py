from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.


def signinPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('user signed in')
            # return redirect('home')
    context = {}
    return render(request, 'sign-in/index.html')
