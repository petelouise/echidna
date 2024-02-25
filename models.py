from peewee import Model, CharField, FloatField, ForeignKeyField
from database import db


class Image(Model):
    hash = CharField(unique=True)
    path = CharField(unique=True)

    class Meta:
        database = db


class ImageFeature(Model):
    image = ForeignKeyField(Image, backref="features")
    energy = FloatField()
    contrast = FloatField()
    correlation = FloatField()
    variance = FloatField()
    local_homogeneity = FloatField()
    sum_average = FloatField()
    sum_variance = FloatField()
    sum_entropy = FloatField()
    entropy = FloatField()
    difference_variance = FloatField()
    difference_entropy = FloatField()
    info_measure_correlation_1 = FloatField()
    info_measure_correlation_2 = FloatField()

    class Meta:
        database = db
