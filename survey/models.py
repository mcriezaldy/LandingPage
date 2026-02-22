from django.db import models

class Survey(models.Model):

    SATISFACTION_CHOICES = [
        ('SP', 'Sangat Puas / Very Satisfied'),
        ('P', 'Puas / Satisfied'),
        ('CP', 'Cukup Puas / Fairly Satisfied'),
        ('TP', 'Tidak Puas / Dissatisfied'),
        ('STP', 'Sangat Tidak Puas / Very Dissatisfied'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    satisfaction = models.CharField(max_length=3, choices=SATISFACTION_CHOICES)
    feedback = models.TextField(blank=True)

    # Checkbox Disclaimer
    agree_law = models.BooleanField(default=False)
    agree_parent = models.BooleanField(default=False)
    agree_ethics = models.BooleanField(default=False)

    # Data dari Ruijie
    mac_address = models.CharField(max_length=20, default="", blank=True)
    ip_address = models.CharField(max_length=20, default="", blank=True)
    ap_ip = models.CharField(max_length=20, default="", blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mac_address}"