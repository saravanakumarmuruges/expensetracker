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
    
    def validate(self, data):
        income_type = data.get('income_type')
        expense_category = data.get('expense_category')
        savings_type = data.get('savings_type')
        selected_columns = [income_type, expense_category, savings_type]
        non_null_columns = [col for col in selected_columns if col is not None]

        if len(non_null_columns) != 1:
            raise serializers.ValidationError({
                "error": "Exactly one of 'income_type', 'expense_category', or 'savings_type' must be provided."
            })

        return data

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