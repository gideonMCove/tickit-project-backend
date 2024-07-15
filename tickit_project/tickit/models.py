from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_max(value):
        '''Determines if value is entered is between 0 and 10'''
        if value < 0 or value > 10000000:
            raise ValidationError(
                _("%(value)s needs to be a value between 0 and 10, including 0 and 10, yada yada yada"),
                params = {"value": value},
            )




class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    parking = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    Date = models.DateTimeField()
    price = models.IntegerField()
    over18 = models.BooleanField(default=True)
    ticket_limit = models.IntegerField(validators=[validate_max])
    image_url = models.CharField(null=True)

    def __str__(self):
        return self.artist




