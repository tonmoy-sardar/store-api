from django.shortcuts import render
from customers.models import *
from rest_framework.generics import*
from customers.serializers import *
from rest_framework.views import *
from django.db.models import Q
from datetime import datetime

class CustomerRegistrationView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersRegistrationSerializer

class EditCustomerView(RetrieveUpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersRegistrationSerializer


class LoginCustomerView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = LoginCustomerSerializer
    def create(self, request, *args, **kwargs):
        request_data = {}
        data= request.data
        login_data = Customers.objects.filter(
            Q(email=data["email_or_phone"]) | Q(contact_no=data["email_or_phone"]),
            password=data["password"])[:1]
        if login_data:
            print('login_data::', login_data)
            for data in login_data:
                data.last_login = datetime.now()
                data.save()
                request_data['email'] = data.email
                request_data['contact_no'] = data.contact_no
                request_data['success'] = 1
        else:
            request_data['success']=0
        return Response(request_data)
