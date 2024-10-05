from django.db import models
from django.utils import timezone

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)

class IncomeType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)

class SavingsType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)

class User(models.Model):
    pass

class TracsactionFact(models.Model):
    user_id= models.IntegerField(primary_key=True)
    amount=models.IntegerField(min=0, max=1000000, null=False)
    transaction_date=models.DateField(default=timezone.now(), null=False, editable=True)
    income_type_id=models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    expense_category_id=models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    savings_type_id=models.ForeignKey(SavingsType, on_delete=models.CASCADE)


