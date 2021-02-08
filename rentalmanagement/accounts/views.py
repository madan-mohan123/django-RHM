from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from dashboard.models import Owner, Tenant, House
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        housepost=request.POST['housepost']
        print(housepost)
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already exist')
         
            return redirect ('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password1,first_name=housepost)
            user.save()
            if user.first_name=="Owner":
                return render(request,'html pages/ownerform.html')
            else:
                return render(request,'html pages/tenantform.html')    
           
            #  return redirect('login')

    else:
        return render(request,'html pages/register.html')

def login(request):
    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
      
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            if user.first_name=="Owner":
                ownerobject=Owner.objects.get(Email=user.email)
                houseobject=House.objects.filter(Owner_Id=ownerobject.id)
               
                request.session['ownerid']=ownerobject.id
                request.session['email']=user.email
               
                return render(request,'html pages/ownerdashboard.html',{'ownobject':ownerobject,'houseobject':houseobject,'ownerid':request.session['ownerid']})
            else:
                tenantobject=Tenant.objects.get(Email=user.email)
                return render(request,'html pages/tenantdashboard.html',{'tenantobject':tenantobject})    
           
        else:
            
            messages.info(request,"Wrong Email or Password")
            return redirect('login')

    else:
       
        return render(request,'html pages/login.html')

def logout(request):
    auth.logout(request)
    try:
        del request.session['ownerid']
        del request.session['email']
    except:
        pass

    return redirect ('/')    