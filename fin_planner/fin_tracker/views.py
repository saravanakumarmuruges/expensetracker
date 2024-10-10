from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import *
from .serializers import *
from .filters import UserFilter, TransactionFactFilter

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserFilter

class TransactionFactView(viewsets.ModelViewSet):
    queryset = TransactionFact.objects.all()
    serializer_class = TransactionFactSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TransactionFactFilter
    
class ExpenseCategoryView(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    
class IncomeTypeView(viewsets.ModelViewSet):
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer

class SavingsTypeView(viewsets.ModelViewSet):
    queryset = SavingsType.objects.all()
    serializer_class = SavingsTypeSerializer
