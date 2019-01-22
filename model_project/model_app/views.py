from django.shortcuts import render


# Create your views here.
def index(request):
    my_dict = {'inserts_contents': "Hello, I'm from model_app"}
    return render(request, 'model_app/index.html', context = my_dict)
