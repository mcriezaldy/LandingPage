from django.db import models

class Survey(models.Model):

    SATISFACTION_CHOICES = [
        ('SP', 'Sangat Puas'),
        ('P', 'Puas'),
        ('CP', 'Cukup Puas'),
        ('TP', 'Tidak Puas'),
        ('STP', 'Sangat Tidak Puas'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    satisfaction = models.CharField(max_length=3, choices=SATISFACTION_CHOICES)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name