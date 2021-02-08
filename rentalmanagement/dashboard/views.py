from django.shortcuts import render
from .models import Owner, Tenant, House
from datetime import datetime
# Create your views here.

def ownerform(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        img=request.POST['pic']

        user=Owner.objects.create(username=username,Email=email,Phone_No=phone_no,img=img)
        user.save()
        return render(request,'html pages/ownerdashboard.html')
    else:    
        return render(request,'html pages/ownerdashboard.html')


def tenantform(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone_no=request.POST['contact']
        members=request.POST['member']
        purpose=request.POST['purpose']
        join=request.POST['join']
        # dat=datetime.strptime(join,'%y-%m-%d')
        address=request.POST['address']
        img=request.POST['picture']

        user=Tenant.objects.create(username=username,Email=email,Phone_No=phone_no,img=img,Members=members,Purpose=purpose,joining_date=join,Address=address,Leave_date='2021-02-11')
        user.save()
        return render(request,'html pages/tenantdashboard.html')
    else:
        return render(request,'html pages/tenantdashboard.html')

def apartment(request):
    if request.method=='POST':
        Rooms=request.POST['Rooms']
        AcRooms=request.POST['AcRooms']
        Room_Type=request.POST['Room_Type']
        City=request.POST['City']
        Address=request.POST['Address']
        Cost=request.POST['Cost']
        Status="Available"
        Description=request.POST['Description']
        img=request.FILES['img']
        Ownerid=request.session['ownerid']
        Offer=request.POST['Offer']
        house=House.objects.create(Rooms=Rooms,AcRooms=AcRooms,Room_Type=Room_Type,City=City,Address=Address,Cost=Cost,Status=Status,Description=Description,img=img,Offer=Offer,Owner_Id=Ownerid)
        house.save()
        return render(request,'html pages/login.html')

    else:
        return render(request,'html pages/owner.html')     