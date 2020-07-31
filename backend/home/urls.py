from django.urls import path
from . import views

urlpatterns = [
    path('statesTotal/', views.allStates, name = 'allStates'),
    path('state/<str:stateName>/', views.specificState, name = 'specificState'),
    path('India/', views.India, name = 'India'),
    path('allPatients/<str:stateName>/', views.allPatients, name = 'allPatients'),
    path('patient/',views.patient, name = 'patient'),
    path('dataBaseFirstEntry/', views.DatabaseFirstEntry, name = 'DatabaseFirstEntry'),
    path('DatabaseUpdate/', views.DatabaseUpdate, name = 'DatabaseUpdate'),
    path('DatabaseTweetsFirstTime/', views.DatabaseTweetsFirstTime, name = 'DatabaseTweetsFirstTime'),
    path('DatabasePatientsFirstTime/', views.DatabasePatientsFirstTime, name = 'DatabasePatientsFirstTime'),
]