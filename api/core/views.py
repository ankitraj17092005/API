from django.shortcuts import render
from .forms import studentForm
from .models import Student,Branch
from django.http import HttpResponse,JsonResponse
from .serializar import studentSerializer
from rest_framework.renderers import JSONRenderer


def home(request):
    if request.method=='POST':
        input_form=studentForm(request.POST)
        if input_form.is_valid():
            input_form.save()
    return render(request,'core/index.html',{'form':studentForm()})
def api(request):
    if request.method=='GET':
        std_id=request.GET.get('id')
        data=Student.objects.filter(id=std_id)
        print("yes")
        serializer=studentSerializer(data,many=True)
        json_dat=JSONRenderer().render(serializer.data)
        return HttpResponse(json_dat,content_type='application/json')
    data=Student.objects.all()
    serializer=studentSerializer(data,many=True)
    json_dat=JSONRenderer().render(serializer.data)
    return HttpResponse(json_dat,content_type='application/json')  