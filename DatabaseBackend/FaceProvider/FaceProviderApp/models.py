from django.db import models


class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    ImageURL = models.TextField()


class LeftEarVector(models.Model):
    LeftEarVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class RightEarVector(models.Model):
    RightEarVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class LeftEyeVector(models.Model):
    LeftEyeVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class RightEyeVector(models.Model):
    RightEyeVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class HairVector(models.Model):
    HairVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class MouthVector(models.Model):
    MouthVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class NoseVector(models.Model):
    NoseVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class LeftEyebrowVector(models.Model):
    LeftEyebrowVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class RightEyebrowVector(models.Model):
    RightEyebrowVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField()


class SuitVector(models.Model):
    SuitVectorID = models.AutoField(primary_key=True)
    ImageID = models.ForeignKey(Image, on_delete=models.CASCADE)
    Vector = models.TextField();
