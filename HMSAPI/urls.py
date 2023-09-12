from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.categoryViews.as_view(), name="Category"),
    path('drug-items/', views.drugItemsViews.as_view(), name="Drugs list"),
]