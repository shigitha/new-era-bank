from django.db import models


# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug =models.SlugField(max_length=250,unique=True)


    class Meta:
        ordering =('name',)
        verbose_name="dictrict"
        verbose_name_plural="districts"

    def __str__(self):
         return '{}'.format(self.name)

class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Account(models.Model):
    name= name=models.CharField(max_length=50)


    def __str__(self):
       return self.name

class Registration(models.Model):
    name= models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    DOB=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    phonenumber= models.CharField(max_length=80,unique=True)
    mail_id=models.EmailField(max_length=250)
    address1=models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    debitcard= models.BooleanField(default=True)
    creditcard = models.BooleanField()
    passbook = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return  '{}'.format(self.name)












