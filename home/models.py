from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class faceitReg(models.Model):
    pname = models.CharField(max_length=122)
    tname = models.CharField(max_length=122)
    femail = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.pname

    
class eleagueReg(models.Model):
    epname = models.CharField(max_length=122)
    etname = models.CharField(max_length=122)
    efemail = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.epname

    