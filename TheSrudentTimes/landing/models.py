from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    text = models.TextField(null=True)

    def __str__(self):
            return "%s %s %s %s" % (self.name, self.email, self.subject, self.text)

