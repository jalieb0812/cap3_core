from django.db import models

# Create your models here.


class All_Cases(models.Model):
    data = models.JSONField(default = dict)


    def __str__(self):
        return f"id:{self.data['id']} name:{self.data['name']}; "
