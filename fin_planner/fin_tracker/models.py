from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, validate_email
from django.core.exceptions import ValidationError

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class IncomeType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class SavingsType(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=100, null=False, default='User')
    email = models.EmailField(max_length=270, unique=True, validators=[validate_email], default='test@test.com')
    available_balance = models.IntegerField(null=False,default=0)
    savings_balance = models.IntegerField(null=False,default=0)
    total_income = models.IntegerField(null=False,default=0)
    total_expense = models.IntegerField(null=False,default=0)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
class TransactionFact(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=200, null=False)
    amount=models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    transaction_date=models.DateField(default=timezone.now, null=False, editable=True)
    income_type=models.ForeignKey(IncomeType, on_delete=models.CASCADE, related_name='incometype', null=True)
    expense_category=models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expensecat', null=True)
    savings_type=models.ForeignKey(SavingsType, on_delete=models.CASCADE, related_name='savingstype', null=True)
    
    def save(self, *args, **kwargs):
       super(TransactionFact, self).save(*args, **kwargs)
       user = self.user
       if self.income_type:
           user.total_income=models.F('total_income') + self.amount
           user.available_balance=models.F('available_balance') + self.amount
           user.save()
       if self.expense_category:
           user.total_expense=models.F('total_expense') + self.amount
           user.available_balance=models.F('available_balance') - self.amount
           user.save()
       if self.savings_type:
           user.savings_balance=models.F('savings_balance') + self.amount
           user.available_balance=models.F('available_balance') - self.amount
           user.save()
    
    def __str__(self):
        return f"{self.user} - {self.description} - {self.amount}"
    
