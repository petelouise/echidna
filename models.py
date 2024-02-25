from peewee import Model, CharField, FloatField, ForeignKeyField
from database import db


class Image(Model):
    hash = CharField(unique=True)
    path = CharField(unique=True)

    class Meta:
        database = db


class ImageFeature(Model):
    image = ForeignKeyField(Image, backref="features")
    contrast = FloatField()
    homogeneity = FloatField()
    energy = FloatField()
    correlation = FloatField()
    entropy = FloatField()
    sum_average = FloatField()
    sum_variance = FloatField()
    sum_entropy = FloatField()
    difference_variance = FloatField()
    difference_entropy = FloatField()
    info_measure_correlation_1 = FloatField()
    info_measure_correlation_2 = FloatField()
    maximal_correlation_coefficient = FloatField()

    class Meta:
        database = db
