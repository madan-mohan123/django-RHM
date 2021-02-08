from django.urls import path
from . import views

urlpatterns=[
   
      path('ownerform',views.ownerform,name='ownerform'),
       path('tenantform',views.tenantform,name='tenantform'),
       path('apartment',views.apartment,name='apartment'),
     
]