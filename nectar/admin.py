# admin.py
from django.contrib import admin
from .models import Site  # Replace with your actual model name

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'discovered_date', 'outreach_date', 'followup_date')
    search_fields = ('company_name', 'meeting_notes', 'next_step')
    list_filter = ('discovered_date', 'outreach_date', 'followup_date')

# If you don't have a custom admin class, you can simply use:
# admin.site.register(Site)
