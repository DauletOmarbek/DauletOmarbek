from  . import views
from django.urls import path

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_details),
    path('companies/<int:id>/vacancies/', views.company_vacancies)

]
