from django.contrib.auth.models import User
# from django.core import serializers as djSerializers
from rest_framework import serializers

from .models import *

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = [
            'website_url',
            'built_with',
            'company_name',
            'company_description',
            'email',
            'phone_number',
            'contact_name',
            'contact_role',
            'contact_method',
            'meeting_notes',
            'next_step',
            'notes',
            'discovered_date',
            'outreach_date',
            'followup_date',
            'meta',
        ]