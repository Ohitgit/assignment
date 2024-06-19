from django.db import models

# Create your models here.

from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name =  models.CharField(max_length=250)
    email_skype = models.CharField(max_length=250)
    service = models.CharField(max_length=250,null=True)
    broker = models.CharField(max_length=250)
    msg = models.TextField()
    country_code = models.CharField(max_length=10)

    mobile_no = models.CharField(max_length=11,
                                      validators=[RegexValidator(regex=r'^\+?1?\d{9,11}$',
                                                                 message="Contact number must be in the format of '+123456789'. Up to 10 digits allowed.")])


    def __str__(self):
        return self.name