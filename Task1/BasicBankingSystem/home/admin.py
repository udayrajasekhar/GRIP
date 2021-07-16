from home.models import Accounts
from django.contrib import admin
from .models import Accounts, Transaction
# Register your models here.
admin.site.register(Accounts)
admin.site.register(Transaction)