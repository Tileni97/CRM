from django.db import models

class Records(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural = "Records"
        ordering = ['-creation_date']    

