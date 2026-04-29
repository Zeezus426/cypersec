from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    how_did_you_hear = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"
