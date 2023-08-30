from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@api_view(['GET'])
def get_header_view(request):
    return Response(HeaderSerializer(Header.objects.last()).data)


@api_view(['GET'])
def get_region_view(request):
    return Response(RegionSerializer(Region.objects.all(), many=True).data)


@api_view(['GET'])
def get_type_view(request):
    return Response(TypeSerializer(Type.objects.all(), many=True).data)


@api_view(['GET'])
def get_doctor_view(request):
    return Response(DoctorSerializer(Doctor.objects.all(), many=True).data)


@api_view(['GET'])
def get_clinic_view(request):
    return Response(ClinicSerializer(Clinic.objects.all(), many=True).data)


@api_view(['GET'])
def get_service_view(request):
    return Response(ServiceSerializer(Service.objects.all(), many=True).data)


@api_view(['GET'])
def get_news_view(request):
    return Response(NewsSerializer(News.objects.all(), many=True).data)


class GetClinicView(generics.ListAPIView):
    """
    GET
    """
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]


class ClinicSearchListApiView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['region', 'rating']
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    def filter_clinic_view(request):
        query = Clinic.objects.all()
        print(query)
        region_id = request.GET.get("region")
        rating_id = request.GET.get("rating")
        if region_id is not None:
            query = query.filter(region_id=region_id)
        if region_id is not None:
            query = query.filter(rating=rating_id)
        ser = ClinicSerializer(query, many=True)
        # clinic = Clinic.objects.last().job.all().count()
        return Response(ser.data)


class GetDoctorView(generics.ListAPIView):
    """
    GET
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]


class DoctorSearchListApiView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['clinic', 'type', 'rating']
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def filter_doctor_view(request, query=None):
        type_id = request.GET.get("type")
        clinic_id = request.GET.get("clinic")
        rating = request.GET.get("rating")

        if type_id is not None:
            query = query.filter(type_id=type_id)
        if clinic_id is not None:
            query = query.filter(clinic_id=clinic_id)
        if rating is not None:
            query = query.filter(rating=rating)
        ser = DoctorSerializer(query, many=True)
        return Response(ser.data)


@api_view(['GET'])
def search_docktor(request):
    name = request.GET['name']
    return Response(DoctorSerializer(Doctor.objects.filter(name__icontains=name), many=True).data)


@api_view(['GET'])
def search_clinic(request):
    name = request.GET['name']
    return Response(ClinicSerializer(Clinic.objects.filter(name__icontains=name), many=True).data)
