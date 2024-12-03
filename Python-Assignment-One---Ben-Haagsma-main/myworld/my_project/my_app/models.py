from django.db import models

class DummyData(models.Model):
    '''basic dummy model, intended to serve as a template for future uses'''
    dummyfield = models.CharField(max_length=100)
