from django.shortcuts import render

from .models import Account
# Create your views here.
def home_screen_view(request):
    context = {}
    accounts = Account.objects.all().order_by('-date_joined')
    context['accounts'] = accounts
    print(accounts)
    return render(request, "personal/home.html", context)
