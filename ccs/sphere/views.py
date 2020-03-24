from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,View
from sphere.models import EnquiryModel
from sphere.forms import EnquiryForm
# Create your views here.
def index(request):
    index1=True
    context={'index':index1}
    return render(request,'index.html',context)
def divya_madam(request):
    return render(request,'divya.html')
def ayushi_madam(request):
    return render(request,'ayushi.html')
def nitignya_sir(request):
    return render(request,'nitignya.html')
def about_us(request):
    about1=True
    context={'about':about1}
    return render(request,'about_us.html',context)
class Enquiry(View):
    def get(self,*args,**kwargs):
        contact=True
        context={'contact':contact}
        return render(self.request,'contact.html',context)
        
