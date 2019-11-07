from django.shortcuts import render
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testapp.permissions import IsReadOnly,SunnyPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]
    permission_classes = [IsAuthenticated,  ]
