from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserView, basename='User')
router.register(r'transaction', TransactionFactView, basename='transaction')
router.register(r'expensecategory', ExpenseCategoryView, basename='expensecategory')
router.register(r'incometype', IncomeTypeView, basename='incometype')
router.register(r'savingstype', SavingsTypeView, basename='savingstype')

urlpatterns = [
    path('', include(router.urls), name='apis')
    
]