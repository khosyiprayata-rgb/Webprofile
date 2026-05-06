from django.db import models

class Feedback(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    kategori = models.CharField(max_length=100, null=True, blank=True)
    pesan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama