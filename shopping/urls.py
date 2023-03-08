from django.urls import path 
from shopping import views

#http://127.0.0.1:8000/

urlpatterns=[

    path('',views.homepage,name="homepage"),
    path('about',views.about,name="about"),
    path('contact_us',views.contact,name="contact"),
]