from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.companies),
    path('companies/<int:comp_id>', views.company_id),
    path('companies/<int:com_id>/vacancies', views.vacancies_in_comp),
    path('vacancies/', views.vacs),
    path('vacancies/<int:vac_id>', views.vacs_id),
    path('vacancies/top_ten', views.vacs_topTen)
]