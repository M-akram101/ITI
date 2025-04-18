from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, db_column="Name")

    def __str__(self):
        return self.name
