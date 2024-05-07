from django.contrib import admin
from home.models import Contact
from home.models import faceitReg
from home.models import eleagueReg

# Register your models here.
admin.site.register(Contact)
admin.site.register(faceitReg)
admin.site.register(eleagueReg)