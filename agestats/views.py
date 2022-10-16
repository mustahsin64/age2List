from django.shortcuts import render
from agestats.models import Unit
from agestats.serializers import UnitSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework import viewsets

class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows unit to be viewed or edited.
    """
    queryset = Unit.objects.all().order_by('name')
    serializer_class = UnitSerializer


@api_view(['GET'])
def unitList(request):
	queryset = Unit.objects.all().order_by('id')
	serializer = UnitSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def unitFilterWithHp(request,hp):
	queryset = Unit.objects.filter(hp=hp)
	serializer = UnitSerializer(queryset,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def unitAdd(request):
	serializer = UnitSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

