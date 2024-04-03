from django.db import models

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        app_label = "core"
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Widget(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
