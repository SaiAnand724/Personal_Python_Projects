from django.shortcuts import render
from django.http import HttpResponse

user_names = {
    'users': [
        {
            'id': 1,
            'name': 'He-mothy',
            'age': 22
        },
        {
            'id': 2,
            'name': 'We-mothy',
            'age': 28
        }
    ]
} 

# Create your views here.
def show_login(request):
    return render(request, 'login.html',  user_names)