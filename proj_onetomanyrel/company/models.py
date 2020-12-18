from django.db import models


# Username: Ankur
# Email address: training@home.com
# Password: testpassword

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=124)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
