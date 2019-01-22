from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict = {'insert_me_help': "Help Page...  I am from AppTwo/views.py ! >:) "}
    return render(request, 'pro_two/index.html', context = my_dict)
