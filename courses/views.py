from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def signin(request):
    if request.user.is_authenticated:
        # return redirect('admin')
        print('hello')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                # return redirect('admin')
            else:
                pass

    return render(request,'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')



