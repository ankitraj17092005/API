from rest_framework import serializers
from .models import Student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

        def create(self,validated_data):
            print(validated_data)
            obj=Student.objects.create(**validated_data)
            return obj
        def update(self,instance,validated_data):
            print(instance)
            print(validated_data)
            instance.name=validated_data.get('name',instance.name)
            instance.roll=validated_data.get('roll',instance.roll)
            instance.gender=validated_data.get('gender',instance.gender)
            instance.summary=validated_data.get('summary',instance.summary)
            instance.branch=validated_data.get('branch',instance.branch)
            instance.save()
            return instance