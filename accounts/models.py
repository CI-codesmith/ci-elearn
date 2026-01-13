
from django.db import models
from core.models import UserProfile, Program, Batch

# Account: OneToOne with UserProfile
class Account(models.Model):
	ACCOUNT_TYPE_CHOICES = [
		('student', 'Student'),
		('intern', 'Intern'),
		('staff', 'Staff'),
	]
	user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='account')
	account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.user_profile} ({self.account_type})"

# FeePlan: linked to Program / Batch
class FeePlan(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='fee_plans')
	batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True, related_name='fee_plans')
	total_amount = models.DecimalField(max_digits=10, decimal_places=2)
	installment_allowed = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.program} - {self.batch or 'All Batches'}: ₹{self.total_amount}"

# Payment: linked to Account
class Payment(models.Model):
	PAYMENT_MODE_CHOICES = [
		('cash', 'Cash'),
		('online', 'Online'),
		('bank', 'Bank'),
	]
	account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payments')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES)
	remarks = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f"{self.account} - ₹{self.amount} on {self.date} ({self.mode})"

# Create your models here.
