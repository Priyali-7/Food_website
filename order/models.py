from django.db import models

# python manage.py inspectdb
# Create your models here.
class ContactData(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10)
    comments = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'contact_data'