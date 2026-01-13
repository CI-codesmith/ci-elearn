
from django.contrib import admin
from .models import Account, FeePlan, Payment

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('user_profile', 'account_type', 'is_active')
	search_fields = ('user_profile__user__username',)
	list_filter = ('account_type', 'is_active')

@admin.register(FeePlan)
class FeePlanAdmin(admin.ModelAdmin):
	list_display = ('program', 'batch', 'total_amount', 'installment_allowed')
	list_filter = ('program', 'batch', 'installment_allowed')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('account', 'amount', 'date', 'mode', 'remarks')
	list_filter = ('mode', 'date')
	search_fields = ('account__user_profile__user__username', 'remarks')
