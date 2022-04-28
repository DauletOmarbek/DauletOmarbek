from rest_framework import serializers
from .models import Vacancy, Company


class VacancyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'description', 'salary', 'company']


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        comp = Company.objects.create(name=validated_data['name'])
        return comp

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'city', 'address']


