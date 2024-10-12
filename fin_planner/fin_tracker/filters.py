import django_filters
from .models import User, TransactionFact


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='name',lookup_expr='icontains')
    email = django_filters.CharFilter(label='email',lookup_expr='icontains')
    available_balance_gte = django_filters.NumberFilter(field_name='available_balance', lookup_expr='gte')
    available_balance_lte = django_filters.NumberFilter(field_name='available_balance', lookup_expr='lte')
    savings_balance_gte = django_filters.NumberFilter(field_name='savings_balance', lookup_expr='gte')
    savings_balance_lte = django_filters.NumberFilter(field_name='savings_balance', lookup_expr='lte')
    total_income_gte = django_filters.NumberFilter(field_name='total_income', lookup_expr='gte')
    total_income_lte = django_filters.NumberFilter(field_name='total_income', lookup_expr='lte')
    total_expense_gte = django_filters.NumberFilter(field_name='total_expense', lookup_expr='gte')
    total_expense_lte = django_filters.NumberFilter(field_name='total_expense', lookup_expr='lte')
    class Meta:
        model= User
        fields = ['name', 'email', 'available_balance', 'savings_balance', 'total_income', 'total_expense']


class TransactionFactFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(label='username', field_name='user__name', lookup_expr='icontains')
    amount_gte = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    amount_lte = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')
    transaction_date = django_filters.DateFromToRangeFilter()
    income_type = django_filters.CharFilter(label='income_type', field_name='income_type__name', lookup_expr='icontains')
    expense_category = django_filters.CharFilter(label='expense_category', field_name='expense_category__name', lookup_expr='icontains')
    savings_type = django_filters.CharFilter(label='savings_type', field_name='savings_type__name', lookup_expr='icontains')
    income_only = django_filters.BooleanFilter(method='only_income', label='income_only')
    expense_only = django_filters.BooleanFilter(method='only_expense', label='expense_only')
    savings_only = django_filters.BooleanFilter(method='only_savings', label='savings_only')
    
    class Meta:
        model= TransactionFact
        fields = ['user', 'amount', 'transaction_date', 'income_type', 'expense_category', 'savings_type']
    
    def only_income(self, queryset, name, value):
        if value:
            return queryset.filter(income_type__isnull=False)
        return queryset
    
    def only_expense(self, queryset, name, value):
        if value:
            return queryset.filter(expense_category__isnull=False)
        return queryset
    
    def only_savings(self, queryset, name, value):
        if value:
            return queryset.filter(savings_type__isnull=False)
        return queryset

