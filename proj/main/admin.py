from django.contrib import admin

from proj.main.models import CreditApplication, Contract, Product, Producer

admin.site.register([CreditApplication, Contract, Product, Producer])
