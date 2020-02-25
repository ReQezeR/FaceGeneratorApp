from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('ImageID', 'ImageURL')


class LeftEarVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeftEarVector
        fields = ('LeftEarVectorID', 'ImageID', 'Vector')


class RightEarVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RightEarVector
        fields = ('RightEarVector', 'ImageID', 'Vector')


class LeftEyeVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeftEyeVector
        fields = ('LeftEyeVector', 'ImageID', 'Vector')


class RightEyeVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RightEyeVector
        fields = ('RightEyeVector', 'ImageID', 'Vector')


class HairVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HairVector
        fields = ('HairVector', 'ImageID', 'Vector')


class MouthVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MouthVector
        fields = ('MouthVector', 'ImageID', 'Vector')


class NoseVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NoseVector
        fields = ('NoseVector', 'ImageID', 'Vector')


class LeftEyebrowVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeftEyebrowVector
        fields = ('LeftEyebrowVector', 'ImageID', 'Vector')


class RightEyebrowVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RightEyebrowVector
        fields = ('RightEyebrowVector', 'ImageID', 'Vector')


class SuitVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SuitVector
        fields = ('SuitVector', 'ImageID', 'Vector')
