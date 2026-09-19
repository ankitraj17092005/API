from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import ProfileForm

# Create your views here.
def index(request):
    #get post request from form data
    if request.method=='POST':
        cre_profile=ProfileForm(request.POST)
        if cre_profile.is_valid():
            cre_profile.save()
            print('profile created')
            return render(request,'api/index.html',{"form":ProfileForm,"status":"profile created"})

    return render(request,'api/index.html',{"form":ProfileForm})