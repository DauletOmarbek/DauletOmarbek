from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Company


def company_list(request):
    company = Company.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'company': company})


def company_details(request, id):
    company = Company.objects.all()
    for x in company:
        if x.id == id + 1:
            return render(request, 'company_details/index.html', {'title': 'Главная страница', 'x': x})
    return HttpResponse('<h2>Not found</h2>')


def company_vacancies(request, id):
    return HttpResponse("<h2>Company_vacancies</h2>")
