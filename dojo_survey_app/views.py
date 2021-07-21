from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "name": "Noelle",
    }
    return render(request,'index.html', context)

def result(request):
    return HttpResponse("placeholder for result")