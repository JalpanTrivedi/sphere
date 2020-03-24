from django.contrib import admin
from django.urls import path
from sphere import views
app_name='sphere'

urlpatterns = [
    path('index',views.index,name='index'),
    path('divya-madam/',views.divya_madam,name="divya-madam"),
    path('ayushi-madam/',views.ayushi_madam,name="ayushi-madam"),
    path('nitignya-sir/',views.nitignya_sir,name="nitignya-sir"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.Enquiry.as_view(),name="contact_us"),
        ]
