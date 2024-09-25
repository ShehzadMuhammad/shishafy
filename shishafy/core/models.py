from django.db.models import Model, CharField


# Create your models here.
class Equipment(Model):
    name = CharField(max_length=200)
