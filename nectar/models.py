from django.db import models
from django.db.models import JSONField

# Core Hive Models
class Site(models.Model):
    # Website Details
    website_url = models.CharField(max_length=255)
    built_with = models.CharField(max_length=255)

    # Company Details
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    
    # Contact Details
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_role = models.CharField(max_length=255)
    contact_method = models.CharField(max_length=255)
    
    meeting_notes = models.CharField(max_length=255)
    next_step = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    # Dates
    discovered_date = models.CharField(max_length=255)
    outreach_date = models.CharField(max_length=255)
    followup_date = models.CharField(max_length=255)

    # Scraping Data
    meta = JSONField(default=dict)

    def __str__(self):
        return "%s" % self.company_name

    class Meta:
        ordering = ['id']
