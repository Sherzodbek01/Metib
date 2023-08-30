from django.urls import path
from .views import *


urlpatterns = [
    path('get-header/', get_header_view),
    path('get-clinic/', get_clinic_view),
    path('get-doctor/', get_doctor_view),
    path('get-region/', get_region_view),
    path('get-type/', get_type_view),
    path('search_docktor/', search_docktor),
    path('search_clinic/', search_clinic),
    path('filter-doctor/', DoctorSearchListApiView.as_view()),
    path('filter-clinic/', ClinicSearchListApiView.as_view()),
]