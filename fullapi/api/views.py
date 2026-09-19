from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .form import ProfileForm
from .serializer import ProfileSerializer
from rest_framework import serializers
from .models import Profile
from rest_framework.renderers import JSONRenderer
from django.views import View
from rest_framework.parsers import JSONParser


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
class apiView(View):
    def get(self,request,id=None):
        if id is not None:
            print('yes',id)
            one_d=Profile.objects.get(id=id)
            serialize_one=ProfileSerializer(one_d)
            return JsonResponse(serialize_one.data,safe=False)
        data=Profile.objects.all()
        serialize=ProfileSerializer(data,many=True)
        # js_d=JSONRenderer().render(serialize.data) #if you use JsonResponse then this renderer are not in use
        return JsonResponse(serialize.data,safe=False)
    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            js_data=JSONParser().parse(request)
            de_serialize=ProfileSerializer(data=js_data)
            if de_serialize.is_valid():
                de_serialize.save()
                msg={'status':'data created'}
                return JsonResponse(msg,safe=False)
            return JsonResponse({'error':de_serialize.errors},safe=False)
    def patch(self,request,*args,**kwargs):
        if request.method=='PATCH':
            js_data=JSONParser().parse(request)
            instance_data=Profile.objects.get(id=js_data['id'])
            js_data.pop('id')
            de_serialize=ProfileSerializer(data=js_data,instance=instance_data,partial=True)
            if de_serialize.is_valid():
                de_serialize.save()
                return JsonResponse({'status':'updated'})
            return JsonResponse(de_serialize.errors)
    def put(self,request,*args,**kwargs):
        if request.method=='PUT':
            js_data=JSONParser().parse(request)
            instance_data=Profile.objects.get(id=js_data['id'])
            js_data.pop('id')
            de_serialize=ProfileSerializer(instance=instance_data,data=js_data)
            if de_serialize.is_valid():
                de_serialize.save()
                return JsonResponse({'staus':'updated'})
            return JsonResponse(de_serialize.errors)

    def delete(self,request,id):
        if request.method=='DELETE':
            try:
                user_data=Profile.objects.get(id=id)
                user_data.delete()
                return JsonResponse({'deleted':'delete'})
            except Exception as e:
                return JsonResponse({'errors':f'{e}'})
