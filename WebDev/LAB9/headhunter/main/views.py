from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Company, Vacancy
import json


def company_list(request):
    companys = Company.objects.all()
    company_json = [company.to_json() for company in companys]
    return JsonResponse(company_json, safe=False)


def company_details(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())


def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        result = []
        vacancys = Vacancy.objects.all()
        vacancy_json = [vacancy.to_json() for vacancy in vacancys]
        for x in vacancy_json:
            if x.company == company.name:
                result.append(x)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(result, safe=False)
