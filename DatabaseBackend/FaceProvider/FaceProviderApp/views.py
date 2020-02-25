from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Wordl")


class ImageViewset(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer


class LeftEarVectorViewset(viewsets.ModelViewSet):
    queryset = models.LeftEarVector.objects.all()
    serializer_class = serializers.LeftEarVectorSerializer


class RightEarVectorViewset(viewsets.ModelViewSet):
    queryset = models.RightEarVector.objects.all()
    serializer_class = serializers.RightEarVectorSerializer


class LeftEyeVectorViewset(viewsets.ModelViewSet):
    queryset = models.LeftEyeVector.objects.all()
    serializer_class = serializers.LeftEyeVectorSerializer


class RightEyeVectorViewset(viewsets.ModelViewSet):
    queryset = models.RightEyeVector.objects.all()
    serializer_class = serializers.RightEyeVectorSerializer


class HairVectorViewset(viewsets.ModelViewSet):
    queryset = models.HairVector.objects.all()
    serializer_class = serializers.HairVectorSerializer


class MouthVectorViewset(viewsets.ModelViewSet):
    queryset = models.MouthVector.objects.all()
    serializer_class = serializers.MouthVectorSerializer


class NoseVectorViewset(viewsets.ModelViewSet):
    queryset = models.NoseVector.objects.all()
    serializer_class = serializers.NoseVectorSerializer


class LeftEyebrowVectorViewset(viewsets.ModelViewSet):
    queryset = models.LeftEyebrowVector.objects.all()
    serializer_class = serializers.LeftEyebrowVectorSerializer


class RightEyebrowVectorViewset(viewsets.ModelViewSet):
    queryset = models.RightEyebrowVector.objects.all()
    serializer_class = serializers.RightEyebrowVectorSerializer


class SuitVectorViewset(viewsets.ModelViewSet):
    queryset = models.SuitVector.objects.all()
    serializer_class = serializers.SuitVectorSerializer