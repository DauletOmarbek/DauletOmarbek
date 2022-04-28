from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('companies/', views.CompanyAPIView.as_view()),
    path('companies/<int:comp_id>', views.CompanyIDAPIView.as_view()),
    path('companies/<int:com_id>/vacancies', views.VacsInCompsVIEW.as_view()),
    path('vacancies/', views.VacanciesAPIView.as_view()),
    path('vacancies/<int:vac_id>', views.VacanciesIDAPIView.as_view()),
]
