
from django.shortcuts import render, redirect
from students.models import Students,Account

# Create your views here.





def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username = username, password = password)
            request.session['userid'] = user.id
            if (user.type == 'student'):
                return redirect('after_login')
            elif(user.type == 'admin'):
                return redirect('admin:index_admin')
        except:
            return render(request, 'login.html',{'message':'username or password is incorrect'})

    return render(request,'login.html')



def index(request):
    return render(request,'index.html')


def after_login(request):
    ss = request.session['userid']
    obj = Account.objects.get(id = ss)
    return render(request,'after_login.html',{'d':obj})