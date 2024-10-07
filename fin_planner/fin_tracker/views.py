from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionFactView(viewsets.ModelViewSet):
    queryset = TransactionFact.objects.all()
    serializer_class = TransactionFactSerializer
    
class ExpenseCategoryView(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    
class IncomeTypeView(viewsets.ModelViewSet):
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer

class SavingsTypeView(viewsets.ModelViewSet):
    queryset = SavingsType.objects.all()
    serializer_class = SavingsTypeSerializer
