from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import *
from .serializers import *
from .filters import UserFilter, TransactionFactFilter
from rest_framework.permissions import IsAuthenticated

class UserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = UserFilter

class TransactionFactView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TransactionFact.objects.all()
    serializer_class = TransactionFactSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TransactionFactFilter
    
class ExpenseCategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    
class IncomeTypeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer

class SavingsTypeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SavingsType.objects.all()
    serializer_class = SavingsTypeSerializer
