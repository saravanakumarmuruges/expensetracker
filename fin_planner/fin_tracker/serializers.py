from rest_framework import serializers
from .models import ExpenseCategory, IncomeType, SavingsType, User, TransactionFact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class TransactionFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionFact
        fields = "__all__"

class SavingsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsType
        fields = "__all__"
        
class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeType
        fields = "__all__"

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"