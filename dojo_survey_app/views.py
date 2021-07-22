from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'index.html')

def result(request):
    context = {
        "name": request.POST["f_name"],
        "dojo_location": request.POST["f_location"],
        "favorite_language": request.POST["f_language"],
        "comment": request.POST["f_comment"],
        "gender": request.POST["gender"],
        "email": request.POST["email"]
    }

    return render(request,'result.html', context)