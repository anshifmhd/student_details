from django.shortcuts import render, redirect
from students.models import Account, Students

# Create your views here.


def add_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(username = username, password = password, type = "admin")
        obj.save()

    return render(request,'add_admin.html')





def index_admin(request):
    return render(request,'index_admin.html')


def view_register(request):
    obj = Students.objects.filter(status = "inactive")
    ob = Students.objects.filter(status = "active")
    return render(request,'view_register.html',{'active_students':ob, 'inactive_students':obj})





def update(request, idd):
    aa = Account.objects.get(id = idd)
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        status = request.POST['status']


        Students.objects.filter(id = idd).update(name = name, place = place, email = email, contact = contact, status = status)
        return redirect('admin:view_register')
    
    print(aa)
    return render(request,'update.html',{'updates':aa})


def register_students(request):
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        username = request.POST['username']
        password = request.POST['password']


        obj = Students( name=name, email=email, contact=contact, place=place, status = 'active')
        obj.save()
        account = Account( username = username, password = password, type = 'student', student_id = obj.id )
        account.save()
    return render(request,'register_students.html')




def register_students1(request):
    if request.method == "POST":
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        username = request.POST['username']
        password = request.POST['password']


        obj = Students( name=name, email=email, contact=contact, place=place, status = 'Inactive')
        obj.save()
        account = Account( username = username, password = password, type = 'student', student_id = obj.id )
        account.save()
    return render(request,'register_students1.html')


def inactive_update(request, inactive_id):
    obj = Students.objects.filter(id = inactive_id).update(status = "inactive")
    return redirect('admin:view_register')


def active_update(request, active_id):
    obj = Students.objects.filter(id = active_id).update(status = "active")
    return redirect('admin:view_register')