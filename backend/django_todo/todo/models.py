from django.db import models
#from dynamorm import DynaModel
#from marshmallow import fields
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    date_created = models.DateField(auto_created=True)

    def __str___(self):
        return self.title

'''
class MyTable(DynaModel):
	class Table:
		name = settings.DB_TABLE
		hash_key = 'created_on'
		read = 25
		write = 5

	class Schema:
		name = fields.String()
		email = fields.Email()
		created_on = fields.DateTime()

'''