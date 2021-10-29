from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import Account



class AccountAdmin(UserAdmin):
	list_display = ('email','username', 'credit')
	search_fields = ('email','username',)
	readonly_fields=('id',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)