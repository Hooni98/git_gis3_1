from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import model


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        model_instance = model()
        model_instance.text = temp
        model_instance.save()
        return render(request, 'accountapp/hello_world.html',
                      context={'model_instance':model_instance})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'get method!'})