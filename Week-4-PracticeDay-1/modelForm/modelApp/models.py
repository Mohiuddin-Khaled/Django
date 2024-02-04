from django.db import models


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=100)
    address = models.TextField(max_length=50)
    date = models.DateTimeField()
    payment_slip = models.FileField(upload_to="files/", blank=False)
    gadget_name = models.CharField(max_length=60)
    ip_address = models.GenericIPAddressField()
    correct_info = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.roll} - {self.name}"
