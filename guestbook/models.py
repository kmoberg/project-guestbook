from email.policy import default

from django.db import models


# Create your models here.

# Guestbook Entry Model
class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    rating = models.IntegerField(default=5)  # Add this field
    irrelevant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def soft_delete(self):
        self.hidden = True
        self.save()

    def restore(self):
        self.hidden = False
        self.save()
