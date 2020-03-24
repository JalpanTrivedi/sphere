from django.db import models

# Create your models here.
class CourceModel(models.Model):
    cource_name=models.CharField(max_length=50,default="")
    cource_fees=models.DecimalField(max_digits=7,decimal_places=2)
    cource_short_detail=models.CharField(max_length=100,blank=True,null=True)
    cource_detail=models.CharField(max_length=500,blank=True,null=True)
    cource_photo=models.ImageField(default="",upload_to="static/cource")
    slug=models.SlugField()

    def __str__(self):
        return self.cource_name


class EnquiryModel(models.Model):
    FirstName=models.CharField(max_length=50,default="")
    LastName=models.CharField(max_length=50,default="")
    PhoneNumber=models.CharField(max_length=50)
    Email = models.EmailField(max_length=254,default="")
    Course=models.CharField(max_length=50,default='OTHER')
    Message=models.CharField(max_length=500,blank=True,null=True)
