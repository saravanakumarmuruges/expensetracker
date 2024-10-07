from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, validate_email

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id} - {self.name}"

class IncomeType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id} - {self.name}"

class SavingsType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id} - {self.name}"

class User(models.Model):
    name = models.CharField(max_length=100, null=False, default='User')
    email = models.EmailField(max_length=270, unique=True, validators=[validate_email], default='test@test.com')
    available_balance = models.IntegerField(null=False,default=0)
    savings_balance = models.IntegerField(null=False,default=0)
    total_income = models.IntegerField(null=False,default=0)
    total_expense = models.IntegerField(null=False,default=0)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
    
class TransactionFact(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=200, null=False)
    amount=models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    transaction_date=models.DateField(default=timezone.now, null=False, editable=True)
    income_type=models.ForeignKey(IncomeType, on_delete=models.CASCADE, related_name='incometype', null=True)
    expense_category=models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expensecat', null=True)
    savings_type=models.ForeignKey(SavingsType, on_delete=models.CASCADE, related_name='savingstype', null=True)
    
    def __str__(self):
        return f"User ID - {self.user} : Spend on - {self.description} : amount of {self.amount}"
