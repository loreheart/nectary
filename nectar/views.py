from django.http import HttpResponse
from rest_framework import permissions, viewsets, response, views

from .models import Site
from .serializers import *


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

def home(request):
    return HttpResponse("Hello, World!")

class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Site.objects.all().order_by('-discovered_date')
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated|ReadOnly]
