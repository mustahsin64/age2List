from django.shortcuts import render
from agestats.models import Unit
from agestats.serializers import UnitSerializer


from rest_framework import viewsets

class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows unit to be viewed or edited.
    """
    queryset = Unit.objects.all().order_by('name')
    serializer_class = UnitSerializer
