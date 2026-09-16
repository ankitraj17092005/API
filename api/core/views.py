from django.shortcuts import render
from .forms import studentForm
from .models import Student,Branch
from django.http import HttpResponse,JsonResponse
from .serializar import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


def home(request):
    if request.method=='POST':
        input_form=studentForm(request.POST)
        if input_form.is_valid():
            input_form.save()
    return render(request,'core/index.html',{'form':studentForm()})
 
@csrf_exempt
def api_post(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'status':'ok'}
            return JsonResponse(msg)
        return JsonResponse(serializer.errors)
    if request.method=='GET':
        s_data=Student.objects.all()
        serialz=studentSerializer(s_data,many=True)

        js_data=JSONRenderer().render(serialz.data)
        return HttpResponse(js_data)
    if request.method == 'PATCH':
        j_d=JSONParser().parse(request)
        u_data=Student.objects.get(id=j_d.get('id'))
        j_d.pop('id')
        serializer=studentSerializer(instance=u_data,data=j_d,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={"status":"updated"}
            return JsonResponse(msg,content_type='application/json',safe=False)
        return JsonResponse(serializer.errors,content_type='application/json',safe=False)
    if request.method=='PUT':
        js_d=JSONParser().parse(request)
        ins_d=Student.objects.get(id=js_d.get('id'))
        js_d.pop('id')
        serialz=studentSerializer(
            instance=ins_d,
            data=js_d

        )
        if serialz.is_valid():
            serialz.save()
            return JsonResponse({'status':'updated'},content_type='application/json',safe=False)
        return JsonResponse(serialz.errors,content_type='application/json',safe=False)
    if request.method=='DELETE':
        json_d=JSONParser().parse(request)
        try:
            usr_d=Student.objects.get(id=json_d.get('id'))
            usr_d.delete()
            return JsonResponse({'status':'deleted'},content_type='application/json',safe=False)
        except Exception as e:
            return JsonResponse({'error':str(e)},content_type='application/json',safe=False)
