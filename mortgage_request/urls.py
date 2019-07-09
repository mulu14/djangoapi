from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mortgage_request import views

urlpatterns = [
    path('mortgages/', views.MortgageList.as_view()),
    path('mortgages/<int:pk>/', views. MortgageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

