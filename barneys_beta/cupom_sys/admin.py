from django.contrib import admin
from .models import *

class PromotionModelAdmin(admin.ModelAdmin):
	list_display=["__str__", "status", "quantidade"]
	list_filter=["título"]
	search_fields=["título", "descrição"]
	class Meta:
		model = Promotion

admin.site.register(Promotion, PromotionModelAdmin) 
