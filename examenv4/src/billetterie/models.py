from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from io import BytesIO
import qrcode

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    clef_unique = models.CharField(max_length=16, unique=True, default=get_random_string(16))

    def __str__(self):
        return self.username

class Offre(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nom

    def count_achats(self):
        return Achat.objects.filter(offre=self).count()

class Achat(models.Model):
    utilisateur = models.ForeignKey(
        'billetterie.Utilisateur',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    offre = models.ForeignKey(
        'billetterie.Offre',
        on_delete=models.CASCADE,
    )
    clef_achat = models.CharField(max_length=16, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.clef_achat:
            self.clef_achat = get_random_string(16)
        super().save(*args, **kwargs)

    def generer_qr_code(self):
        clef_finale = f"{self.utilisateur.clef_unique}_{self.clef_achat}"
        qr = qrcode.make(clef_finale)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
